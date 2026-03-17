import json, re, os, requests
from datetime import datetime

# CONFIGURATION
DB_FILE = "data.json"
TARGET_COUNT = 500  # Email me when we hit this
NICHE_URL = "https://example-niche-site.com/directory" # Replace with target

def harvest():
    # Load or init database
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            db = json.load(f)
    else:
        db = {"leads": [], "metadata": {"last_run": ""}}

    # Scraping Logic
    try:
        response = requests.get(NICHE_URL, timeout=10)
        # Regex to find emails
        found_emails = re.findall(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}', response.text.lower())
        
        # Filter duplicates
        existing = {l['email'] for l in db['leads']}
        new_count = 0
        for email in set(found_emails):
            if email not in existing:
                db['leads'].append({
                    "email": email,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "source": NICHE_URL
                })
                new_count += 1
        
        db['metadata']['last_run'] = datetime.now().isoformat()
        db['metadata']['total'] = len(db['leads'])
        
        # Save vault
        with open(DB_FILE, 'w') as f:
            json.dump(db, f, indent=2)
            
        print(f"Success: Found {new_count} new leads. Total: {len(db['leads'])}")
        return len(db['leads'])
        
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    count = harvest()
    # Output for GitHub Actions trigger
    if count >= TARGET_COUNT:
        print("TRIGGER_EMAIL=true")
    else:
        print("TRIGGER_EMAIL=false")
