
from core.config import TAKEOVER_SIGNATURES

def check_takeover(cname):
    """
    Checks if the CNAME matches known takeover signatures.
    Returns the service name if vulnerable, else None.
    """
    if not cname:
        return None
    
    for fingerprint, service in TAKEOVER_SIGNATURES.items():
        if fingerprint in cname:
            return service
    return None
