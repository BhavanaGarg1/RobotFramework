#find the second largest value in this list without using in built functions

nums = [3, 1, 10, 11, 4, 5, 6]

# Remove duplicates if needed
unique_nums = list(set(nums))

# Sort in descending order
unique_nums.sort(reverse=True)

print(unique_nums[0])

print(len(unique_nums))
# Second largest
if len(unique_nums) >= 2:
    print("Second largest number is:", unique_nums[1])
else:
    print("No second largest number found.")

 # 2nd approach:
nums = [1, 3, 10, 11, 4, 5, 6]

# Initialize first and second largest
first = second = float('-inf')

print(first)

for num in nums:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

if second != float('-inf'):
    print("Second largest number is:", second)
else:
    print("No second largest number found.")

# for num in range(len(nums)):
#     if nums[num] == second:
#         del nums[num]
#         break
#
# print(nums)

# largest = arr[0]
# second = None
#
# for i in arr:
#     if i > largest:
#         largest = i
# for i in arr:
#     if i != largest:
#         if second is None or i > second:
#             second = i
# for i in range(len(arr)):
#     if arr[i] == second:
#         del arr[i]
#         break
#
# print(largest)
# print(second)
# print(arr)
