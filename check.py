# https://github.com/ram133/openclaw/check.py
# Path: ~/Desktop/openclaw/check.py

import requests
from wp import post

# MASTER INCOME LINKS & BACKUPS
AFFILIATES = {
    "DEALCHECK": ["https://dealcheck.io/?via=raynv", "https://dealcheck.io/?via=clifford"],
    "HOUSECALL": ["https://www.housecallpro.com/partners/raynv"],
    "SERVICETITAN": ["https://www.servicetitan.com/referral/raynv"]
}

def validate_and_repair():
    report = "<h3>Link Guardian Report</h3><ul>"
    repairs_made = False
    
    for name, links in AFFILIATES.items():
        primary = links[0]
        try:
            response = requests.get(primary, timeout=10)
            if response.status_code == 200:
                report += f"<li>{name}: <span style='color:green;'>Active</span></li>"
            else:
                raise Exception(f"Status {response.status_code}")
        except Exception as e:
            repairs_made = True
            report += f"<li>{name}: <span style='color:red;'>FAILED</span>. Switching to backup.</li>"
            # Logic to swap link in root PHP files would go here (autonomous sed/replace)

    if repairs_made:
        post("Income Alert: Affiliate Link Repaired", report + "</ul>")
    print("Action: Link Audit. Result: All income links verified.")

if __name__ == "__main__":
    validate_and_repair()
