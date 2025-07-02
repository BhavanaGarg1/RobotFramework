#4 List of toys at a different price and you have 50rs how many toys you can buy

toys = [15, 20, 10, 25, 5, 30, 8]  # Toy prices
budget = 50

# Sort toys by price (buy cheapest first)
toys.sort()

count = 0
total = 0

for price in toys:
    if total + price <= budget:
        total += price
        count += 1
    else:
        break

print(f"You can buy {count} toys for ₹{total} within your ₹{budget} budget.")
