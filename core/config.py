
# Configuration and Constants

# Common ports to scan during active reconnaissance
COMMON_PORTS = [21, 22, 25, 53, 80, 443, 445, 3306, 8080, 8443]

# Subdomain Takeover Signatures (Fingerprints)
# Service CNAME -> Service Name
TAKEOVER_SIGNATURES = {
    "github.io": "GitHub Pages",
    "herokuapp.com": "Heroku",
    "s3.amazonaws.com": "AWS S3",
    "azurewebsites.net": "Azure Web App",
    "bitbucket.io": "Bitbucket",
    "pantheon.io": "Pantheon",
    "myshopify.com": "Shopify",
    "tumblr.com": "Tumblr",
    "wordpress.com": "WordPress",
    "teamwork.com": "Teamwork"
}
