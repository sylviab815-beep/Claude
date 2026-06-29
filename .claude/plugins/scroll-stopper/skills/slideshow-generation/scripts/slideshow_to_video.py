#!/usr/bin/env python3
"""Turn a slideshow folder into a 9:16 TikTok-ready MP4.

Takes slide_01.jpg..slide_NN.jpg in a folder, applies Ken Burns zoom +
crossfade transitions, and optionally adds audio:
  * background music (--music), and/or
  * AI voiceover narration (--vo-text "<script>" or --vo-audio file.mp3).

Voiceover is OPTIONAL and only available if the user connected ElevenLabs in
`/scroll-stopper-setup` (config: has_elevenlabs + elevenlabs_api_key). When a
voiceover is used, the slideshow auto-paces so its length matches the narration,
and any background music is ducked underneath. Final audio is loudness-normalized
to ~-14 LUFS (TikTok standard).

Usage:
    python3 slideshow_to_video.py "/path/to/Slideshow-01" [--music track.mp3]
    python3 slideshow_to_video.py "/path/to/Slideshow-01" --vo-text "She's spent 11 years hiding..."
    python3 slideshow_to_video.py "/path/to/Slideshow-01" --vo-text "..." --music track.mp3
    python3 slideshow_to_video.py "/path/to/Slideshow-01" --vo-audio narration.mp3
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    import config as ss_config
except Exception:
    ss_config = None

OUT_W, OUT_H = 1080, 1920
FPS = 30
DEFAULT_DURATION = 3.0
DEFAULT_FADE = 0.6
MIN_SLIDE_DURATION = 1.6
ELEVEN_TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128"
DEFAULT_VOICE = "XB0fDUnXU5powFXDhCwa"  # Charlotte


def resolve_ffmpeg() -> str:
    """Prefer imageio-ffmpeg's bundled binary, fall back to system ffmpeg."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        pass
    system = shutil.which("ffmpeg")
    if system:
        return system
    print("ffmpeg not found. Install: pip3 install imageio-ffmpeg", file=sys.stderr)
    sys.exit(2)


def media_duration(ffmpeg: str, path: Path) -> float:
    """Get a media file's duration in seconds by parsing ffmpeg's stderr."""
    out = subprocess.run([ffmpeg, "-i", str(path)], capture_output=True, text=True).stderr
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", out)
    if not m:
        return 0.0
    h, mm, ss = m.groups()
    return int(h) * 3600 + int(mm) * 60 + float(ss)


def generate_voiceover(text: str, out_path: Path, api_key: str, voice_id: str) -> bool:
    """Generate narration via ElevenLabs. Returns True on success."""
    body = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.8,
                           "style": 0.35, "use_speaker_boost": True},
    }).encode("utf-8")
    req = urllib.request.Request(
        ELEVEN_TTS_URL.format(voice=voice_id), data=body, method="POST",
        headers={"xi-api-key": api_key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            out_path.write_bytes(resp.read())
        return out_path.stat().st_size > 1000
    except Exception as e:
        print(f"ElevenLabs voiceover failed: {e}", file=sys.stderr)
        return False


def build_filter_complex(n_slides: int, duration: float, fade: float) -> tuple[str, str]:
    """Return (filter_complex, final_label). n_slides >= 1."""
    zoom_frames = int(duration * FPS)
    parts: list[str] = []
    for i in range(n_slides):
        if i % 2 == 0:
            zoom_expr = "min(zoom+0.0006,1.12)"
        else:
            zoom_expr = "if(lte(zoom,1.0),1.12,max(zoom-0.0006,1.0))"
        parts.append(
            f"[{i}:v]"
            f"scale={OUT_W*2}:{OUT_H*2}:force_original_aspect_ratio=increase,"
            f"crop={OUT_W*2}:{OUT_H*2},"
            f"zoompan=z='{zoom_expr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={zoom_frames}:s={OUT_W}x{OUT_H}:fps={FPS},"
            f"setsar=1,format=yuv420p[v{i}]"
        )
    if n_slides == 1:
        return ";".join(parts), "v0"
    prev = "v0"
    total_prev = duration
    for i in range(1, n_slides):
        label = f"x{i}" if i < n_slides - 1 else "vout"
        offset = total_prev - fade
        parts.append(
            f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={offset:.3f}[{label}]"
        )
        prev = label
        total_prev += duration - fade
    return ";".join(parts), "vout"


def detect_genre(folder: Path) -> str:
    """Pull the genre from the slideshow's hooks.json, then manifest.txt."""
    hooks = folder / "hooks.json"
    if hooks.exists():
        try:
            plan = json.loads(hooks.read_text())
            g = plan.get("genre")
            if not g and plan.get("slides"):
                g = plan["slides"][0].get("text_style")
            if g:
                return g
        except Exception:
            pass
    manifest = folder / "manifest.txt"
    if manifest.exists():
        m = re.search(r"Genre:\s*(.+)", manifest.read_text())
        if m:
            return m.group(1).strip()
    return "dark_romance"


def resolve_auto_music(folder: Path, n_slides: int, per_slide: float) -> str | None:
    """Generate a genre-matched track via fal.ai. Returns path str, or None on failure."""
    try:
        import fal_music
    except Exception as e:
        print(f"Auto music unavailable ({e}); rendering silent.", file=sys.stderr)
        return None
    genre = detect_genre(folder)
    out = folder.parent / "music" / f"{fal_music.slugify(genre)}_fal.mp3"
    duration = max(20.0, n_slides * per_slide + 2)
    try:
        path = fal_music.generate_music(genre, out, duration=duration)
        return str(path)
    except Exception as e:
        print(f"Auto music generation failed ({e}); rendering silent.", file=sys.stderr)
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Slideshow folder containing slide_*.jpg")
    parser.add_argument("--music", help="Optional background music: a file path (mp3/wav/m4a), or 'auto' to generate a genre-matched instrumental via fal.ai (uses FAL_KEY)")
    parser.add_argument("--vo-text", help="Narration script — generates AI voiceover via ElevenLabs")
    parser.add_argument("--vo-audio", help="Pre-made voiceover audio file (skips ElevenLabs)")
    parser.add_argument("--voice-id", help="ElevenLabs voice ID (overrides config default)")
    parser.add_argument("--duration", type=float, default=DEFAULT_DURATION,
                        help=f"Seconds per slide (default {DEFAULT_DURATION}; ignored when a voiceover sets the pace)")
    parser.add_argument("--fade", type=float, default=DEFAULT_FADE,
                        help=f"Crossfade seconds (default {DEFAULT_FADE})")
    parser.add_argument("--output", help="Output MP4 path (default: <folder>.mp4 in parent)")
    args = parser.parse_args()

    ffmpeg = resolve_ffmpeg()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Not a folder: {folder}", file=sys.stderr)
        return 2

    slides = sorted(folder.glob("slide_*.jpg"))
    if not slides:
        print(f"No slide_*.jpg in {folder}", file=sys.stderr)
        return 2
    n = len(slides)

    output = Path(args.output).expanduser().resolve() if args.output else folder.parent / f"{folder.name}.mp4"
    output.parent.mkdir(parents=True, exist_ok=True)

    cfg = ss_config.load() if ss_config else {}
    tmpdir = Path(tempfile.mkdtemp(prefix="ss_vo_"))

    # ---- Resolve 'auto' music: generate a genre-matched track via fal.ai ----
    if args.music and args.music.strip().lower() == "auto":
        args.music = resolve_auto_music(folder, n, args.duration) or None

    # ---- Resolve voiceover (optional) ----
    vo_path = None
    if args.vo_audio:
        vo_path = Path(args.vo_audio).expanduser().resolve()
        if not vo_path.exists():
            print(f"Voiceover audio not found: {vo_path}", file=sys.stderr)
            return 2
    elif args.vo_text:
        api_key = cfg.get("elevenlabs_api_key", "")
        if not api_key:
            print("Voiceover requested but no ElevenLabs key set. Run /scroll-stopper-setup "
                  "and add ElevenLabs, or use --vo-audio with your own file.", file=sys.stderr)
            return 2
        voice = args.voice_id or cfg.get("elevenlabs_voice_id") or DEFAULT_VOICE
        vo_path = tmpdir / "voiceover.mp3"
        print("Generating ElevenLabs voiceover...")
        if not generate_voiceover(args.vo_text, vo_path, api_key, voice):
            return 2

    # ---- Pace slides to the narration when a voiceover is present ----
    duration = args.duration
    if vo_path:
        vo_dur = media_duration(ffmpeg, vo_path)
        if vo_dur > 0:
            # total = n*duration - (n-1)*fade  ->  solve duration for total == vo_dur (+0.4s tail)
            duration = max(MIN_SLIDE_DURATION, (vo_dur + 0.4 + (n - 1) * args.fade) / n)

    total_duration = n * duration - (n - 1) * args.fade

    # ---- Inputs ----
    cmd: list[str] = [ffmpeg, "-y", "-hide_banner", "-loglevel", "error"]
    for s in slides:
        cmd += ["-loop", "1", "-t", str(duration), "-i", str(s)]

    music_idx = vo_idx = None
    next_idx = n
    if args.music:
        music_path = Path(args.music).expanduser().resolve()
        if not music_path.exists():
            print(f"Music file not found: {music_path}", file=sys.stderr)
            return 2
        cmd += ["-i", str(music_path)]
        music_idx = next_idx
        next_idx += 1
    if vo_path:
        cmd += ["-i", str(vo_path)]
        vo_idx = next_idx
        next_idx += 1

    filter_complex, final_label = build_filter_complex(n, duration, args.fade)
    fade_out_st = max(0, total_duration - 1.2)

    # ---- Audio graph ----
    audio_map = None
    extra_audio_args: list[str] = []
    if vo_idx is not None and music_idx is not None:
        # Duck music under the voiceover, mix, normalize.
        filter_complex += (
            f";[{music_idx}:a]volume=0.16,afade=t=in:st=0:d=0.8,"
            f"afade=t=out:st={fade_out_st:.3f}:d=1.0[mbg];"
            f"[{vo_idx}:a]afade=t=in:st=0:d=0.2[voa];"
            f"[mbg][voa]amix=inputs=2:duration=longest:dropout_transition=0,"
            f"loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
        )
        audio_map = "[aout]"
    elif vo_idx is not None:
        filter_complex += (
            f";[{vo_idx}:a]afade=t=in:st=0:d=0.2,"
            f"loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
        )
        audio_map = "[aout]"

    cmd += ["-filter_complex", filter_complex, "-map", f"[{final_label}]"]

    if audio_map is not None:
        cmd += ["-map", audio_map, "-c:a", "aac", "-b:a", "192k"]
    elif music_idx is not None:
        # Music-only (unchanged behavior)
        cmd += [
            "-map", f"{music_idx}:a",
            "-af", f"afade=t=in:st=0:d=0.8,afade=t=out:st={fade_out_st:.3f}:d=1.0",
            "-c:a", "aac", "-b:a", "192k", "-shortest",
        ]

    cmd += [
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-r", str(FPS),
        "-t", f"{total_duration:.3f}",
        str(output),
    ]

    if vo_path:
        vo_label = "ElevenLabs narration" if args.vo_text else Path(str(vo_path)).name
    else:
        vo_label = "(none)"
    print(f"Slides:    {n}")
    print(f"Duration:  {total_duration:.1f}s @ {FPS}fps → {OUT_W}x{OUT_H}")
    print(f"Voiceover: {vo_label}")
    print(f"Music:     {Path(args.music).name if args.music else '(silent — add in TikTok/Reels)'}")
    print(f"Output:    {output}")
    print("Encoding...")

    result = subprocess.run(cmd, capture_output=True, text=True)
    shutil.rmtree(tmpdir, ignore_errors=True)
    if result.returncode != 0:
        print(result.stderr[-4000:], file=sys.stderr)
        return result.returncode

    print(f"Done: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
