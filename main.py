import os
import argparse
from colorama import Fore, init
from modules.args_parser import parse_arguments
from modules.banners import clear_and_print, display_help
from modules.torrent import is_tool_installed, install_nodejs, install_webtorrent_cli, magnet_to_torrent

# Initialize colorama for colored output
init(autoreset=True)

if __name__ == "__main__":
    # Display banners
    clear_and_print()
    display_help()

    args = parse_arguments()

    magnet_link = args.url
    output_dir = args.output

    if not is_tool_installed("node"):
        print(Fore.YELLOW + "Node.js is not installed. Installing Node.js...")
        install_nodejs()

    if not is_tool_installed("npm"):
        print(Fore.RED + "Error: npm is not available. Please ensure Node.js installation was successful.")
        exit(1)

    if not is_tool_installed("webtorrent"):
        print(Fore.YELLOW + "webtorrent-cli is not installed. Installing webtorrent-cli...")
        install_webtorrent_cli()

    try:
        torrent_file = magnet_to_torrent(magnet_link, output_dir)
        print(Fore.GREEN + f"Process completed successfully! Torrent saved at: {torrent_file}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
