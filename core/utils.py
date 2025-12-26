
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""
    {Fore.CYAN}#########################################################
    #                                                       #
    #          PYSUBENUM v1.2 - OFFENSIVE EDITION           #
    #          ----------------------------------           #
    #     Features: Passive Recon + CNAME Analysis          #
    #               + Subdomain Takeover Check              #
    #     Dev: Bellamy                                      #
    #                                                       #
    #########################################################{Style.RESET_ALL}
    """
    print(banner)

def print_status(message, type="info"):
    if type == "info":
        print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")
    elif type == "success":
        print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")
    elif type == "warning":
        print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")
    elif type == "error":
        print(f"{Fore.RED}[-] {message}{Style.RESET_ALL}")
        