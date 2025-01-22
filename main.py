import os
from colorama import Fore, Style, init
from modules.args_parser import parse_arguments
from modules.banners import clear_and_print, display_help
from modules.torrent import is_tool_installed, install_nodejs, install_webtorrent_cli, magnet_to_torrent

# Initialize colorama for colored output
init(autoreset=True)

def main():
    # Clear the console and display the banner
    clear_and_print()

    # Parse command-line arguments
    args = parse_arguments()

    # Display custom help if no arguments are provided
    if not args.url:
        print(Fore.RED + "Error: Magnet link is required.")
        display_help()
        exit(1)

    # Set output directory with a default fallback
    output_dir = args.output or "torrents"

    # Check and install required tools
    if not is_tool_installed("node"):
        print(Fore.YELLOW + "Node.js is not installed. Installing Node.js...")
        install_nodejs()

    if not is_tool_installed("npm"):
        print(Fore.RED + "Error: npm is not available. Please ensure Node.js installation was successful.")
        exit(1)

    if not is_tool_installed("webtorrent"):
        print(Fore.YELLOW + "webtorrent-cli is not installed. Installing webtorrent-cli...")
        install_webtorrent_cli()

    # Process the magnet link and generate the torrent file
    try:
        torrent_file = magnet_to_torrent(args.url, output_dir)
        print(Fore.GREEN + f"Process completed successfully! Torrent saved at: {torrent_file}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
