
import requests
from core.utils import print_status

def fetch_crtsh(domain):
    print_status("Extracting data from: crt.sh...", "warning")
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subdomains = set()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PySubEnum/1.2"}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name_value = entry['name_value']
                for sub in name_value.split("\n"):
                    subdomains.add(sub)
    except Exception:
        pass
    return subdomains

def fetch_hackertarget(domain):
    print_status("Extracting data from: HackerTarget...", "warning")
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    subdomains = set()
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            lines = response.text.split("\n")
            for line in lines:
                if "," in line:
                    subdomains.add(line.split(",")[0])
    except Exception:
        pass
    return subdomains
