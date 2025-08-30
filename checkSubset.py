# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of elements in set A (not strictly needed for the solution)
    n = int(input())
    # Read the elements of set A and convert to a set of integers
    set_a = set(map(int, input().split()))

    # Read the number of elements in set B (not strictly needed for the solution)
    m = int(input())
    # Read the elements of set B and convert to a set of integers
    set_b = set(map(int, input().split()))

    # Check if set A is a subset of set B and print the boolean result
    print(set_a.issubset(set_b))

# Sample Input
#
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output
#
# True
# False
# False