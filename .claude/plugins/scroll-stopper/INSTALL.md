# Installing Scroll Stopper

A 5-minute setup. You only do this once.

---

## 1. Install Claude Code

If you don't have it: https://claude.com/claude-code

Open Terminal (Mac) or PowerShell (Windows) and run `claude` once to confirm it's installed.

---

## 2. Install Python dependencies

In Terminal:

```bash
pip3 install fal-client Pillow python-docx ebooklib pypdf imageio-ffmpeg dropbox
```

If that errors with "command not found", install Python 3.9+ first from python.org.

---

## 3. Get a fal.ai API key (only if using AI mode)

If you plan to use **cover-only mode**, skip this step entirely — no API key needed.

For AI image generation (~$0.05 per slide):

1. Go to https://fal.ai → sign up (free)
2. Dashboard → API Keys → create one
3. Copy the key (looks like `keyid:secret`)
4. In Terminal:

   ```bash
   echo 'export FAL_KEY=your-key-id:your-secret' >> ~/.zshrc
   source ~/.zshrc
   ```

   (If you're on bash: replace `~/.zshrc` with `~/.bashrc`.)

5. Verify: `echo $FAL_KEY` should print your key.

---

## 3a. (Optional) Get a free Pixabay Music API key

If you want Scroll Stopper to auto-download free, royalty-free music tracks for your videos:

1. Go to https://pixabay.com/accounts/register/ → create a free account (no credit card)
2. Go to https://pixabay.com/api/docs/ → your API key shows on the page when you're logged in
3. Copy it. You'll paste during `/scroll-stopper-setup`.

Pixabay Music is **free for commercial use, no attribution required**. Genuinely free, not "free with credit." Use it as your default music source unless you specifically want a custom AI-generated track.

---

## 3b. (Optional) Get a Dropbox access token — for Metricool scheduling

If you'll use **Metricool** (or any bulk scheduler) to post your videos, Scroll Stopper can auto-upload your MP4s to Dropbox and give you back direct URLs the scheduler can fetch. (Google Drive links don't work with Metricool — Dropbox does.)

Skip this if you'll upload videos manually one at a time.

1. Go to https://www.dropbox.com/developers/apps
2. Click **Create app**
3. Choose **Scoped access** → **Full Dropbox** → name it `Scroll Stopper` → Create
4. **Permissions tab** → check these four boxes, then click Submit:
   - `files.content.write`
   - `files.content.read`
   - `sharing.write`
   - `sharing.read`
5. **Settings tab** → scroll down to **Generated access token** → set expiration to **No expiration** → click **Generate**
6. Copy the token (looks like a long string of letters/numbers)
7. Paste it when `/scroll-stopper-setup` asks for it

The token gives Scroll Stopper permission to upload videos *into* a `Scroll-Stopper/` folder in your Dropbox. It cannot read other folders.

---

## 4. Install the Scroll Stopper plugin

### Mac — double-click installer

1. Unzip the Scroll Stopper download
2. **Double-click `Install-Scroll-Stopper.command`** in Finder
3. Wait for "Done. Scroll Stopper is installed." then close the window

**First-time macOS warning** ("can't be opened because it's from an unidentified developer"):
- Right-click the file → **Open** → click **Open** in the dialog
- Mac remembers this choice forever after

### Windows — double-click installer

1. Unzip the Scroll Stopper download
2. **Double-click `Install-Scroll-Stopper.bat`** in File Explorer
3. Wait for "Done. Scroll Stopper is installed." then press any key

**First-time Windows warning** ("Windows protected your PC"):
- Click **More info** → **Run anyway**

### Manual install (only if the installer won't run)

```bash
mkdir -p ~/.claude/plugins
cp -R scroll-stopper ~/.claude/plugins/
```

---

## 5. Run the setup wizard

Open Claude Code and type:

```
/plugins
```

Confirm Scroll Stopper appears in the list. Then:

```
/scroll-stopper-setup
```

It'll ask you about 7 things:

1. Where to save your slideshows (Google Drive, Dropbox, iCloud, local — your call)
2. Where you keep your books (so it can scan and detect genres in bulk)
3. Default mode: AI / cover / hybrid
4. Which platforms you post to (just for logging)
5. Font preference (use genre defaults, or pick one font for everything)
6. Music default for video render (silent / auto-generate / your own / ask each time)
7. CSV log path + which columns matter to you

Done. You're ready.

---

## 6. Generate your first slideshow

```
/create-slideshow path/to/your-book.epub 3 7
```

Or if you set a library folder in step 5, just:

```
/scan-library
```

…then pick which books to make slideshows for.

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'fal_client'`** — re-run `pip3 install fal-client`.

**`FAL_KEY not set`** — your shell didn't pick up the export. Run `source ~/.zshrc` and try again, or restart Terminal.

**Installer won't open on Mac** — right-click → Open (instead of double-click) to bypass the unidentified-developer warning the first time.

**Installer says "scroll-stopper folder not found"** — you double-clicked before fully unzipping. Unzip the download, then double-click from inside the unzipped folder where `scroll-stopper/` sits next to the installer.

**Fonts look wrong** — Scroll Stopper looks for fonts in `/Library/Fonts`, `~/Library/Fonts`, and `/System/Library/Fonts`. If the genre's recommended font isn't installed, it falls back to system defaults.

**Slideshow looks plain** — make sure your manuscript has at least 3000 words. Cover mode works on any manuscript since it doesn't need style cues.
