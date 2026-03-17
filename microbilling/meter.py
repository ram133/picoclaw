import yaml
import json

def measure(usage_data):
    with open('process_usage.yaml', 'r') as f:
        config = yaml.safe_load(f)
    # logic to calculate units
    units = usage_data.get('count', 0) * config.get('rate', 1)
    return units

if __name__ == "__main__":
    test_data = {'count': 10}
    print(f"Units: {measure(test_data)}")
