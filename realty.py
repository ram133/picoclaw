# https://github.com/ram133/picoclaw/realty.py
# Path: picoclaw/realty.py

import json
import csv
from wp import post  # Autonomous integration with your relay script

def calculate_lead_score(price, est_rent, days_on_market):
    """Autonomously scores real estate leads for ROI potential."""
    if price <= 0 or est_rent <= 0: return 0
    rent_ratio = price / (est_rent * 12)
    score = (100 / rent_ratio) + (50 / (days_on_market + 1))
    return round(score, 2)

def process_listings(listings):
    """Processes, ranks, and prepares leads for WordPress."""
    scored = []
    for prop in listings:
        prop['lead_score'] = calculate_lead_score(
            prop.get('price', 0), prop.get('est_rent', 0), prop.get('days_on_market', 0)
        )
        scored.append(prop)
    return sorted(scored, key=lambda x: x['lead_score'], reverse=True)

if __name__ == "__main__":
    # Sample data for execution
    sample_data = [
        {"address": "123 Alpha St", "price": 250000, "est_rent": 2100, "days_on_market": 5},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    
    results = process_listings(sample_data)
    
    # Constructing the WordPress post content
    wp_content = "<h2>Hot Realty Leads Found</h2><ul>"
    for res in results:
        wp_content += f"<li><strong>{res['address']}</strong>: Score {res['lead_score']} | Price: ${res['price']}</li>"
    wp_content += "</ul>"
    
    # Autonomous Post Execution
    post("Daily Realty Lead Report", wp_content)        {"address": "456 Beta Ave", "price": 400000, "est_rent": 2800, "days_on_market": 30},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    results = process_listings(sample_data)
    for res in results:
        print(f"Score: {res['lead_score']} | {res['address']}")
    export_leads(results)        {"address": "456 Beta Ave", "price": 400000, "est_rent": 2800, "days_on_market": 30},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    results = process_listings(sample_data)
    for res in results:
        print(f"Score: {res['lead_score']} | {res['address']}")
    export_leads(results)            property.get('days_on_market', 0)
        )
        property['lead_score'] = score
        scored_listings.append(property)
    
    return sorted(scored_listings, key=lambda x: x['lead_score'], reverse=True)

if __name__ == "__main__":
    # Sample data representing incoming real estate leads
    sample_data = [
        {"address": "123 Alpha St", "price": 250000, "est_rent": 2100, "days_on_market": 5},
        {"address": "456 Beta Ave", "price": 400000, "est_rent": 2800, "days_on_market": 30},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    
    results = process_listings(sample_data)
    
    # Display results and autonomously export to CSV
    for res in results:
        print(f"Score: {res['lead_score']} | Address: {res['address']}")
    
    export_leads(results)
