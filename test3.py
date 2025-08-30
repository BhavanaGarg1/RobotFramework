# Write a Python function that reads a CSV file containing columns
# user_id, product_id, and purchase_amount.
# The function should calculate and return a dictionary where each key is a
# user_id and the value is a tuple containing the total purchase amount and
# the count of unique products purchased by that user.
# Example CSV Content:
# user_id,product_id,purchase_amount
# 1,101,30
# 1,102,40
# 2,101,20
# 1,101,30
# Example Output:
# {
# 1: (100, 2), # 30 + 40 + 30, 2 unique products
# 2: (20, 1)# 20, 1 unique product
# }

import csv
from collections import defaultdict


def analyze_purchases(csv_file_path = "C:\\Users\\dinesh garg\\PycharmProjects\\Interviews\\test.csv"):
    user_data = defaultdict(lambda: {'total': 0, 'products': set()})

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = int(row['user_id'])
            product_id = int(row['product_id'])
            purchase_amount = float(row['purchase_amount'])

            user_data[user_id]['total'] += purchase_amount
            user_data[user_id]['products'].add(product_id)

    # Convert to final format: user_id -> (total_purchase_amount, unique_product_count)
    result = {
        user_id: (int(data['total']), len(data['products']))
        for user_id, data in user_data.items()
    }

    return result

result = analyze_purchases('test.csv')
print(result)
