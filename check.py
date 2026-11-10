import json
from pathlib import Path

policy = json.loads(Path("retry-policy.json").read_text())
assert type(policy["maxAttempts"]) is int and 1 <= policy["maxAttempts"] <= 5, "maxAttempts must be an integer from 1 to 5"
assert type(policy["timeoutSeconds"]) is int and policy["timeoutSeconds"] > 0, "timeoutSeconds must be a positive integer"
print("Retry policy is valid")
