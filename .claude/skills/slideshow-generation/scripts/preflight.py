#!/usr/bin/env python3
"""Preflight check: verifies FAL_KEY and required packages."""
import os
import sys
import importlib

REQUIRED = {
    "fal_client": "fal-client",
    "PIL": "Pillow",
    "docx": "python-docx",
    "ebooklib": "ebooklib",
    "pypdf": "pypdf",
}

def main() -> int:
    missing_pkgs = []
    for mod, pkg in REQUIRED.items():
        try:
            importlib.import_module(mod)
        except ImportError:
            missing_pkgs.append(pkg)

    key_ok = bool(os.environ.get("FAL_KEY"))

    print("=== Slideshow Hook Generator — Preflight ===")
    print(f"FAL_KEY: {'OK' if key_ok else 'MISSING'}")
    for pkg in REQUIRED.values():
        status = "MISSING" if pkg in missing_pkgs else "OK"
        print(f"  {pkg}: {status}")

    if missing_pkgs:
        print(f"\nInstall missing packages:\n  pip3 install {' '.join(missing_pkgs)}")
    if not key_ok:
        print("\nSet your fal.ai API key:\n  export FAL_KEY=keyid:secret")

    return 0 if key_ok and not missing_pkgs else 1


if __name__ == "__main__":
    sys.exit(main())
