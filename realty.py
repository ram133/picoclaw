# https://github.com/ram133/picoclaw/realty.py
# Path: picoclaw/realty.py

import json
from wp import post

# AUTONOMOUS MONETIZATION LINKS
DEALCHECK_URL = "https://dealcheck.io/?via=clifford" # Example structure
BUILDIUM_URL = "https://buildium.com/affiliate-lead"

def calculate_lead_score(price, est_rent, days_on_market):
    if price <= 0 or est_rent <= 0: return 0
    rent_ratio = price / (est_rent * 12)
    score = (100 / rent_ratio) + (50 / (days_on_market + 1))
    return round(score, 2)

def generate_report(results):
    """Formats lead data with income-generating affiliate links."""
    html = "<h2>High-Yield Real Estate Leads</h2>"
    html += "<p><em>Analyzed by PicoClaw Autonomous Engine</em></p><hr>"
    
    for res in results:
        html += f"""
        <div style='border:1px solid #ccc; padding:10px; margin-bottom:10px;'>
            <h3>{res['address']}</h3>
            <p><strong>Price:</strong> ${res['price']} | <strong>Score:</strong> {res['lead_score']}</p>
            <a href='{DEALCHECK_URL}' style='color:blue;'>Analyze this deal in-depth &rarr;</a>
        </div>
        """
    
    html += f"""
    <hr>
    <h3>Investor Resources</h3>
    <ul>
        <li><a href='{BUILDIUM_URL}'>Best Property Management for these Leads</a></li>
        <li><a href='{DEALCHECK_URL}'>Free ROI Calculator Tool</a></li>
    </ul>
    <p>[end]</p>
    """
    return html

if __name__ == "__main__":
    sample_data = [
        {"address": "123 Alpha St", "price": 250000, "est_rent": 2100, "days_on_market": 5},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    
    results = sorted(
        [dict(p, lead_score=calculate_lead_score(p['price'], p['est_rent'], p['days_on_market'])) for p in sample_data],
        key=lambda x: x['lead_score'], reverse=True
    )
    
    report_content = generate_report(results)
    post("Daily Realty ROI Report", report_content)
