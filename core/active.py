
import socket
import re
import requests
import dns.resolver
from core.config import COMMON_PORTS
from core.takeover import check_takeover

def get_dns_records(domain):
    """
    Retrieves A and CNAME records using dnspython.
    """
    records = {"ip": [], "cname": None}
    resolver = dns.resolver.Resolver()
    resolver.timeout = 2
    resolver.lifetime = 2

    try:
        answers = resolver.resolve(domain, 'A')
        for rdata in answers:
            records["ip"].append(rdata.to_text())
    except: pass

    try:
        answers = resolver.resolve(domain, 'CNAME')
        for rdata in answers:
            records["cname"] = rdata.target.to_text().rstrip(".")
    except: pass

    return records

def scan_target(subdomain, scan_ports_flag):
    """
    Performs active checks: DNS resolution, Takeover check, HTTP title, Port scan.
    """
    if "*" in subdomain: return None

    # 1. DNS Resolution
    dns_data = get_dns_records(subdomain)
    
    if not dns_data["ip"]:
        return None

    result = {
        "subdomain": subdomain,
        "ip": dns_data["ip"],
        "cname": dns_data["cname"],
        "takeover": None,
        "http_info": "",
        "ports": []
    }

    # 2. Takeover Check
    takeover_service = check_takeover(dns_data["cname"])
    if takeover_service:
        result["takeover"] = takeover_service

    # 3. HTTP Info
    target_ip = dns_data["ip"][0]
    try:
        url = f"https://{subdomain}"
        r = requests.get(url, timeout=3, allow_redirects=True, verify=False)
    except:
        try:
            url = f"http://{subdomain}"
            r = requests.get(url, timeout=3, allow_redirects=True)
        except: r = None
    
    if r:
        match = re.search(r'<title>(.*?)</title>', r.text, re.IGNORECASE | re.DOTALL)
        title = match.group(1).strip()[:50] if match else "No Title"
        result["http_info"] = f"[{r.status_code}] {title}"

    # 4. Port Scanning
    if scan_ports_flag:
        for port in COMMON_PORTS:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target_ip, port)) == 0:
                    result["ports"].append(port)
                s.close()
            except: pass

    return result
