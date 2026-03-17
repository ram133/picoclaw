import json
from datetime import datetime

def record(entry):
    entry['timestamp'] = datetime.now().isoformat()
    with open('usage.log', 'a') as f:
        f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    record({'user': 'user_01', 'action': 'api_call', 'cost': 1})
