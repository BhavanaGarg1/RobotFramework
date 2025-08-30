import json
from faker import Faker

fake = Faker()

# Generate list of user dictionaries
users = []
for _ in range(5):
    user = {
        "id": fake.unique.random_int(min=1, max=1000),
        "name": fake.name(),
        "email": fake.unique.email(),
        "address": fake.address().replace("\n", ", "),
        "is_active": fake.boolean(),
    }
    users.append(user)

# Write to JSON file
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("users.json created.")
