
import sys
import argparse
import concurrent.futures
from colorama import Fore, Style
import urllib3

# Core Imports
from core.utils import print_banner, print_status
from core.passive import fetch_crtsh, fetch_hackertarget
from core.active import scan_target

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    # Example usage text for Help Menu
    examples = f"""{Fore.YELLOW}Examples:{Style.RESET_ALL}
      python3 main.py -d example.com
      python3 main.py -d example.com -c (Active Check & Takeover)
      python3 main.py -d example.com -c -p -t 50 (Full Scan with Ports)
      python3 main.py -d example.com -o report.txt
    """

    parser = argparse.ArgumentParser(
        description=f"{Fore.CYAN}PySubEnum v1.2 - Advanced Subdomain & Takeover Scanner{Style.RESET_ALL}",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-d", "--domain", help="Target Domain (e.g., example.com)")
    parser.add_argument("-o", "--output", help="Save results to a file")
    parser.add_argument("-c", "--check", help="Perform Active Scan (DNS, HTTP, Takeover)", action="store_true")
    parser.add_argument("-p", "--ports", help="Scan common ports (Requires -c)", action="store_true")
    parser.add_argument("-t", "--threads", help="Thread count (Default: 20)", type=int, default=20)
    
    # Check if no arguments provided (Nmap style)
    if len(sys.argv) == 1:
        print_banner()
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    print_banner()

    # --- PHASE 1: PASSIVE ---
    print(f"\n{Fore.BLUE}[ PHASE 1: PASSIVE RECONNAISSANCE ]{Style.RESET_ALL}")
    all_sub = set()
    all_sub.update(fetch_crtsh(args.domain))
    all_sub.update(fetch_hackertarget(args.domain))
    
    if not all_sub:
        print_status("No subdomains found.", "error")
        sys.exit()

    print_status(f"Total unique subdomains found: {len(all_sub)}", "success")
    
    final_results = []

    # --- PHASE 2: ACTIVE ---
    if args.check:
        print(f"\n{Fore.BLUE}[ PHASE 2: ACTIVE SCANNING & TAKEOVER ANALYSIS ]{Style.RESET_ALL}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
            future_to_sub = {executor.submit(scan_target, sub, args.ports): sub for sub in all_sub}
            
            for future in concurrent.futures.as_completed(future_to_sub):
                data = future.result()
                if data:
                    # Output formatting
                    out = f"{Fore.GREEN}[+] {data['subdomain']}{Style.RESET_ALL} -> {data['ip']}"
                    
                    if data['cname']:
                        out += f" | CNAME: {Fore.CYAN}{data['cname']}{Style.RESET_ALL}"
                    
                    if data['takeover']:
                        out += f"\n    {Fore.RED}[!!!] POTENTIAL TAKEOVER DETECTED: {data['takeover']} [!!!]{Style.RESET_ALL}"
                    
                    if data['http_info']:
                        out += f"\n    Web: {data['http_info']}"
                    
                    if data['ports']:
                        out += f" | Ports: {data['ports']}"
                    
                    print(out + "\n" + "-"*40)
                    final_results.append(data)
    else:
        for sub in sorted(all_sub):
            print(sub)
            final_results.append({"subdomain": sub})

    # --- SAVE TO FILE ---
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for item in final_results:
                line = f"Domain: {item['subdomain']}"
                if 'ip' in item: line += f", IP: {item['ip']}"
                if item.get('takeover'): line += f" [VULN: {item['takeover']}]"
                f.write(line + "\n")
        print_status(f"Results saved to '{args.output}'", "success")

if __name__ == "__main__":
    main()
    