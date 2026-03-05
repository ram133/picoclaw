# https://github.com/ram133/picoclaw/realty.py
# Path: picoclaw/realty.py

import json

def calculate_lead_score(price, est_rent, days_on_market):
    """
    Autonomously scores real estate leads for income potential.
    High score = High ROI / Fast turnaround.
    """
    # Safety check added to prevent division by zero
    if price <= 0 or est_rent <= 0: return 0
    
    # Calculate Price-to-Rent Ratio (Lower is usually better for cash flow)
    rent_ratio = price / (est_rent * 12)
    
    # Score calculation: Weighted towards low ratio and low days on market
    score = (100 / rent_ratio) + (50 / (days_on_market + 1))
    return round(score, 2)

def process_listings(listings):
    scored_listings = []
    for property in listings:
        score = calculate_lead_score(
            property.get('price', 0), 
            property.get('est_rent', 0), 
            property.get('days_on_market', 0)
        )
        property['lead_score'] = score
        scored_listings.append(property)
    
    # Sort by highest score first
    return sorted(scored_listings, key=lambda x: x['lead_score'], reverse=True)

if __name__ == "__main__":
    # Example autonomous execution with sample data
    sample_data = [
        {"address": "123 Alpha St", "price": 250000, "est_rent": 2100, "days_on_market": 5},
        {"address": "456 Beta Ave", "price": 400000, "est_rent": 2800, "days_on_market": 30},
        {"address": "789 Gamma Rd", "price": 150000, "est_rent": 1400, "days_on_market": 2}
    ]
    
    results = process_listings(sample_data)
    # Refined output to show all ranked leads
    for res in results:
        print(f"Score: {res['lead_score']} | Address: {res['address']}")
