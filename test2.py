# Proposed a brute force approach, indicating a need for more efficient solutions
# knowledge.
# Write a Python function that takes a list of dictionaries representing transactions,
# with each dictionary containing transaction_id, amount, and
# timestamp (in ISO 8601 format). The function should return a dictionary with
# months as keys (in "YYYY-MM" format) and the total transaction amount for each month
# as values.
# Input:
# transactions = [
# {"transaction_id": 1, "amount": 100, "timestamp": "2024-01-15T08:00:00Z"},
# {"transaction_id": 2, "amount": 200, "timestamp": "2024-01-20T10:00:00Z"},
# {"transaction_id": 3, "amount": 150, "timestamp": "2024-02-05T09:00:00Z"}
# ]
# Output:
# {
# "2024-01": 300,
# "2024-02": 150
# }

from datetime import datetime

def monthly_transaction_totals(transactions):
    result = {}

    for txn in transactions:
        # Extract timestamp and convert to 'YYYY-MM'
        ts = txn["timestamp"]
        month = datetime.fromisoformat(ts.replace("Z", "+00:00")).strftime("%Y-%m")

        # Add amount to that month's total
        if month in result:
            result[month] += txn["amount"]
        else:
            result[month] = txn["amount"]

    return result

transactions = [
    {"transaction_id": 1, "amount": 100, "timestamp": "2024-01-15T08:00:00Z"},
    {"transaction_id": 2, "amount": 200, "timestamp": "2024-01-20T10:00:00Z"},
    {"transaction_id": 3, "amount": 150, "timestamp": "2024-02-05T09:00:00Z"}
]

print(monthly_transaction_totals(transactions))
