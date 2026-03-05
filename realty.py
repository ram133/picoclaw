# https://github.com/ram133/picoclaw/realty.py
# Path: picoclaw/realty.py

import json
import csv

def calculate_lead_score(price, est_rent, days_on_market):
    """Autonomously scores real estate leads for ROI potential."""
    if price <= 0 or est_rent <= 0: return 0
    rent_ratio = price / (est_rent * 12)
    # Weighted: Lower price-to-rent ratio and fewer days on market = higher score
    score = (100 / rent_ratio) + (50 / (days_on_market + 1))
    return round(score, 2)

def export_leads(listings, filename="hot_leads.csv"):
    """Saves top leads to CSV for immediate income-generating use."""
    if not listings: return
    with open(filename, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=listings[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(listings)
    print(f"Success: Exported {len(listings)} leads to {filename}")

def process_listings(listings):
    """Processes and ranks listings by score."""
    scored = []
    for prop in listings:
        prop['lead_score'] = calculate_lead_score(
            prop.get('price', 0), prop.get('est_rent', 0), prop.get('days_on_market', 0)
        )
        scored.append(prop)
    return sorted(scored, key=lambda x: x['lead_score'], reverse=True)

if __name__ == "__main__":
    sample_data = [
        {"address": "123 Alpha St", "price": 250000, "est_rent": 2100, "days_on_market": 5},
        {"address": "456 Beta Ave", "price": 400000, "est_rent": 2800, "days_on_market": 30},
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
