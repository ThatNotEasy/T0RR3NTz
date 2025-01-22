import os, time
from sys import stdout
from colorama import Fore, Style

# =========================================================================================================== #

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# =========================================================================================================== #

def banners():
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"████████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███╗   ██╗████████╗███████╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗╚════██╗████╗  ██║╚══██╔══╝╚══███╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"   ██║   ██║   ██║██████╔╝██████╔╝ █████╔╝██╔██╗ ██║   ██║     ███╔╝ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"   ██║   ██║   ██║██╔══██╗██╔══██╗ ╚═══██╗██║╚██╗██║   ██║    ███╔╝  \n")
    stdout.write(""+Fore.LIGHTRED_EX +"   ██║   ╚██████╔╝██║  ██║██║  ██║██████╔╝██║ ╚████║   ██║   ███████╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝\n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦══════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/THATNOTEASY                        "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[T0RR3NTZ] - {Fore.GREEN}Magnet to Torrent Converter 🚀 - {Fore.RED}[V1.0] \n{Fore.RESET}")

# =========================================================================================================== #

def clear_and_print():
    time.sleep(1)
    clear_screen()
    banners()

# =========================================================================================================== #

def display_help():
    """Display custom help message with emoji."""
    print(
        f"{Fore.RED}.++" + "═" * 100 + f"++.{Style.RESET_ALL}\n"
        f"{Fore.CYAN}{'Option':<40}{'Description':<90}{Style.RESET_ALL}\n"
        f"{Fore.RED}.++" + "═" * 100 + f"++.{Style.RESET_ALL}\n"
        f"  {Fore.GREEN}-u, --url{' ' * 22}{Style.RESET_ALL}URL of the magnet link 🌐\n"
        f"  {Fore.GREEN}-o, --output{' ' * 19}{Style.RESET_ALL}Name of the output file 💾\n"
        f"{Fore.RED}.++" + "═" * 100 + f"++.{Style.RESET_ALL}\n"
        f"  {Fore.GREEN}-h, --help{' ' * 21}{Style.RESET_ALL}Show this help message and exit ❓\n"
        f"{Fore.RED}.++" + "═" * 100 + f"++.{Style.RESET_ALL}\n"
    )
    
# =========================================================================================================== #
