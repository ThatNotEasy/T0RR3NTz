# Torrent Downloader Script

A Python script to download torrent files from magnet links using `webtorrent-cli`. This script automates the setup of necessary dependencies like Node.js, npm, and `webtorrent-cli`.

---

## Features
- Converts magnet links to torrent files.
- Automatically installs required dependencies (`Node.js`, `npm`, `webtorrent-cli`).
- Supports specifying custom output directories.
- Displays a progress bar for installations.
- User-friendly help message.

---

## Requirements
- Python 3.7 or higher.
- `npm` (Node.js package manager) must be available or installed automatically by the script.
- `webtorrent-cli` will be installed if not already available.

---

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/ThatNotEasy/T0RR3NTz
    cd T0RR3NTz
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
Run the script with the following options:

### Command Line Options
| Option                | Description                        |
|-----------------------|------------------------------------|
| `-u`, `--url`         | URL of the magnet link (required). |
| `-o`, `--output`      | Directory to save the torrent file. Default is `torrents`. |
| `-h`, `--help`        | Display the help message.          |

---
