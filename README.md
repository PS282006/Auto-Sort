# Auto-Sort 🧹

A zero-dependency file organization script that automatically organizes crowded folders (like `~/Downloads`) into structured subdirectories by file type.

## What It Does
Auto-Sort inspects target directories, reads file extension signatures, and routes files into categorized folders:
- **Code:** `.py`, `.js`, `.html`, `.dart`, etc.
- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Videos:** `.mp4`, `.mov`, `.mkv`

## Why I Built It
As a developer testing packages, downloading datasets, and downloading APKs/scripts, the local downloads directory quickly turns into clutter. I built Auto-Sort as a simple background automation script to keep developer workspaces organized without installing heavy commercial cleaner apps.

## Tech Stack
- **Language:** Python 3.x
- **Core Modules:** `os` (Filesystem introspection), `shutil` (Atomic file movement)
- **Dependencies:** None (Pure Python standard library)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/PS282006/Auto-Sort.git
   cd Auto-Sort
   ```
2. Execute the script:
   ```bash
   python3 autosort.py
   ```
3. *(Optional)* Schedule it via macOS `crontab` or `launchd` to run automatically on system boot or daily schedules.
