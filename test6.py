#Finding missing number from an array

def find_missing_number(arr):
    n = len(arr) + 1  # Because one number is missing, the actual size should be +1
    total = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)     # Sum of the elements in the given array
    return total - actual_sum  # The difference is the missing number


arr = [1, 2, 4, 5, 6]
print("Missing number is:", find_missing_number(arr))

#A version that handles multiple missing numbers
def find_multiple_missing_numbers(arr, n):
    full_set = set(range(1, n + 1))  # All expected numbers
    actual_set = set(arr)            # Numbers we actually have
    missing_numbers = list(full_set - actual_set)  # Set difference
    return sorted(missing_numbers)   # Return in order

arr = [1, 2, 4, 6, 7, 10]
n = 10
print("Missing numbers are:", find_multiple_missing_numbers(arr, n))


#Or one that works for unsorted arrays or arrays starting from 0

def find_missing_number(arr):
    start = min(arr)
    end = max(arr)
    return sum(range(start, end + 1)) - sum(arr)

arr = [12, 10, 14, 15, 13, 16]  # Missing 11
print("Missing number is:", find_missing_number(arr))
