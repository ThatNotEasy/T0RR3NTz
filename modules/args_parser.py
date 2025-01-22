import argparse
from colorama import Fore, Style

def parse_arguments():
    """Parse and return command-line arguments."""
    # Create the ArgumentParser with no default help and no description
    parser = argparse.ArgumentParser(
        add_help=False,  # Disable default help
        usage="",  # Suppress the default usage message
    )

    # Add arguments (these will not include the default descriptions)
    parser.add_argument("-u", "--url", help=argparse.SUPPRESS)
    parser.add_argument("-o", "--output", help=argparse.SUPPRESS)
    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS
    )

    return parser.parse_args()
