# return a list of square of each element in a list

def square_elements(arr):
    result = []
    for num in arr:
        result.append(num * num)
    return result

#fine max element in an array

def find_max(arr):
    max_ele = arr[0]
    for num in arr:
        if num > max_ele:
            max_ele = num
    return max_ele

# function to return a sum of all the elements in an array

def total_sum(arr):
    total = sum(arr)
    return total

def total_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example usage
arr = [1, 2, 3, 4, 5]
print("Total sum:", total_sum(arr))


# check dups

def has_dups(arr):
    return len(arr) != len(set(arr))

#max product of two elements in an array

def max_product(arr):
    arr.sort()
    return max(arr[0] * arr[1],arr[-1] * arr[-2])


# has pair with sum
def has_pair_with_sum (nums,target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False

nums = [1,2,3,9]
target = 8

# even or odd number checker

def check_even_odd(num):
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#Prime Number checker:

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num **0.5)+1):
        if num % i == 0:
            return False
    return True

#Print all prime in range

def primes_in_range(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num,end=" ")

#flattened the list
nested = [[1,2],[3,4]]
flat = [item for sublist in nested for item in sublist]

#remove vowels from string
s= "Automation"
no_vowels =''.join([c for c in s if c.lower not in 'aeiou'])
print(no_vowels)

#find first non repeating character
from collections import Counter
s = "automation"
counts = Counter(s)
for ch in s:
    if counts[ch]== 1:
        print(ch)
        break




