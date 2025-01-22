import os
import platform
import time
from colorama import Fore, init
from tqdm import tqdm

# Initialize colorama for colored output
init(autoreset=True)


def is_tool_installed(tool):
    """Check if a tool is installed by verifying the version output."""
    try:
        result = os.popen(f"{tool} --version").read().strip()
        return bool(result)
    except Exception as e:
        print(Fore.RED + f"Error checking {tool}: {e}")
        return False


def show_progress_bar(duration, message, color=Fore.CYAN):
    """Display a progress bar with a colored message."""
    print(color + message + Fore.RESET)
    for _ in tqdm(range(duration), desc=message, bar_format="{l_bar}{bar} | {remaining}s", colour="cyan"):
        time.sleep(1)


def install_nodejs():
    """Check the Node.js version and install it only if required."""
    try:
        # Get the installed Node.js version
        version_output = os.popen("node -v").read().strip()
        print(Fore.GREEN + f"Detected Node.js version: {version_output}")

        # Extract the major version number
        major_version = int(version_output.lstrip("v").split(".")[0])

        # Check if the version is sufficient
        if major_version >= 18:
            print(Fore.GREEN + "Node.js version is sufficient. Skipping installation.")
            return
        else:
            print(Fore.YELLOW + f"Node.js version {version_output} is outdated. Installing a newer version...")
    except Exception as e:
        print(Fore.YELLOW + "Node.js is not installed or version detection failed. Installing Node.js...")

    # Proceed with Node.js installation if not installed or outdated
    system = platform.system().lower()

    print(Fore.CYAN + "Downloading and installing Node.js...")
    if system == "windows":
        url = "https://nodejs.org/dist/latest/node-v18.15.0-x64.msi"
        installer_path = "node_installer.msi"
        os.system(f"curl -o {installer_path} {url}")
        show_progress_bar(5, "Installing Node.js on Windows...", Fore.YELLOW)
        os.system(f"msiexec /i {installer_path} /quiet /norestart")
        os.remove(installer_path)
    elif system == "linux":
        show_progress_bar(5, "Installing Node.js on Linux...", Fore.YELLOW)
        os.system("curl -fsSL https://deb.nodesource.com/setup_18.x | bash -")
        os.system("sudo apt-get install -y nodejs")
    elif system == "darwin":
        show_progress_bar(5, "Installing Node.js on macOS...", Fore.YELLOW)
        os.system("brew install node")
    else:
        print(Fore.RED + f"Unsupported platform: {system}")
        raise SystemError("Cannot install Node.js on this platform.")

    print(Fore.GREEN + "Node.js installation completed.")


def install_webtorrent_cli():
    """Install webtorrent-cli using npm."""
    print(Fore.CYAN + "Installing webtorrent-cli using npm...")
    show_progress_bar(5, "Installing webtorrent-cli...", Fore.YELLOW)

    if os.system("npm install -g webtorrent-cli") != 0:
        print(Fore.RED + "Failed to install webtorrent-cli. Please check your npm configuration.")
        raise RuntimeError("webtorrent-cli installation failed.")

    print(Fore.GREEN + "webtorrent-cli installed successfully.")


def magnet_to_torrent(magnet_link, output_dir="torrents"):
    """Convert a magnet link to a torrent file using webtorrent-cli."""
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    torrent_file_name = "download.torrent"
    torrent_path = os.path.join(output_dir, torrent_file_name)

    print(Fore.CYAN + "Converting magnet link to torrent file using webtorrent-cli...")
    if os.system(f"webtorrent download {magnet_link} --out {output_dir} --dump-torrent") != 0:
        print(Fore.RED + "Error during torrent conversion. Ensure webtorrent-cli is properly installed.")
        raise RuntimeError("Failed to convert magnet link to torrent file.")

    print(Fore.GREEN + f"Torrent file saved to: {torrent_path}")
    return torrent_path
