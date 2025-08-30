import json
import re

# Load JSON data
with open("users.json", "r") as f:
    users = json.load(f)

# Validation results
errors = []

# Validation rules
for user in users:
    if not isinstance(user.get("id"), int):
        errors.append(f"Invalid ID: {user}")

    if not user.get("name") or len(user["name"]) < 3:
        errors.append(f"Invalid name: {user}")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", user.get("email", "")):
        errors.append(f"Invalid email: {user}")

    if "address" not in user or not user["address"]:
        errors.append(f"Missing address: {user}")

    if not isinstance(user.get("is_active"), bool):
        errors.append(f"'is_active' should be boolean: {user}")

# Print results
if errors:
    print("Validation failed:")
    for err in errors:
        print(" -", err)
else:
    print("All records are valid!")
