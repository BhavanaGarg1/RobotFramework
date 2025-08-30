# Read the number of elements for set A (not strictly needed for the set creation)
input()
# Read the elements of set A
A = set(map(int, input().split()))

# Read the number of operations
N = int(input())

# Loop through each operation
for _ in range(N):
    # Read the operation type and dummy value
    operation_info = input().split()
    operation_type = operation_info[0]

    # Read the elements of the other set
    another_set = set(map(int, input().split()))

    # Perform the specified mutation based on the operation_type
    if operation_type == 'update':
        A.update(another_set)
    elif operation_type == 'intersection_update':
        A.intersection_update(another_set)
    elif operation_type == 'difference_update':
        A.difference_update(another_set)
    elif operation_type == 'symmetric_difference_update':
        A.symmetric_difference_update(another_set)

# Print the sum of elements in the final set A
print(sum(A))



# Sample Input
#
#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66
# Sample Output
#
# 38