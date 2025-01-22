import argparse
from colorama import Fore, Style

def parse_arguments():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Torrent Downloader Script",
        add_help=False,
        usage="python main.py -u <magnet_url> -o <output_directory>"
    )

    # Add custom arguments with default values
    parser.add_argument("-u", "--url", help="URL of the magnet link 🌐", required=True)
    parser.add_argument("-o", "--output", help="Name of the output file 💾", default="torrents")
    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit ❓"
    )

    return parser.parse_args()
