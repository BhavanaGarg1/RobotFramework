from collections import Counter

tot_num_shoes = int(input("Enter num of shoes in the shop :"))
shoe_sizes_list = input("The available sizes are : ").split()
print(shoe_sizes_list)
size_pairs_count = Counter(shoe_sizes_list)
print(size_pairs_count)
tot_num_customers = int(input("Num of customers : "))

total_amt = 0

for i in range(tot_num_customers):
    try:
        size, rate = input("shoe size and its rate : ").split()
        rate = int(rate)
        if size_pairs_count[size] > 0:
            size_pairs_count[size] -= 1
            total_amt += rate
    except ValueError:
        print("Invalid input. Please enter exactly 2 values: size and rate.")
print("Total Amount Earned:", total_amt)

# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
# 200