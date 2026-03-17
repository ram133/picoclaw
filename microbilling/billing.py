import time
import json
import os

class Billing:
    def __init__(self, storage_path="credits.json"):
        self.storage_path = storage_path
        self.rates = {
            "input_tokens": 0.00001,
            "output_tokens": 0.00003,
            "api_call": 0.01
        }
        self.user_data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return {"balance": 0.0, "history": []}

    def _save_data(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.user_data, f, indent=4)

    def add_credits(self, amount):
        self.user_data["balance"] += amount
        self._save_data()
        return self.user_data["balance"]

    def deduct_usage(self, service_type, quantity=1):
        cost = self.rates.get(service_type, 0) * quantity
        if self.user_data["balance"] >= cost:
            self.user_data["balance"] -= cost
            self.user_data["history"].append({
                "timestamp": time.time(),
                "service": service_type,
                "cost": cost
            })
            self._save_data()
            return True, cost
        return False, 0

    def get_balance(self):
        return self.user_data["balance"]
