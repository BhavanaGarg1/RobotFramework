arr = [5, 1, 9, 6, 9, 2]

unique_num = set(arr)
print(unique_num)

unique_num_list = list(unique_num)
unique_num_list.sort(reverse=True)
print(unique_num_list)

second_largest = unique_num_list[1]
print(second_largest)

unique_num_list.pop(1)
print(unique_num_list)
#
# unique_num_list.remove(second_largest)
# print(unique_num_list)

# second approach
arr = [5, 1, 9, 6, 9, 2]

# Step 1: Find largest
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i

# Step 2: Find second largest
second = None
for i in arr:
    if i != largest:
        if second is None or i > second:
            second = i

# Step 3: Remove first occurrence of second largest
for i in range(len(arr)):
    if arr[i] == second:
        del arr[i]
        break

print("After deleting second largest:", arr)
