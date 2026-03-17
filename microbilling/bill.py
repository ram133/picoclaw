import yaml

def charge(user_id, amount):
    with open('process_charge.yaml', 'r') as f:
        rules = yaml.safe_load(f)
    # execution logic for billing
    print(f"Charging {user_id}: {amount} credits based on {rules.get('type')}")
    return True

if __name__ == "__main__":
    charge("user_01", 5)
