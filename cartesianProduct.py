from itertools import product

input_A = list(map(int, input("Num 1 :").split()))
input_B = list(map(int, input("Num 2 :").split()))

print(*list(product(input_A, input_B)))

# '*' is unpacking operator.It unpacks the elements of the iterable returned by
# list(product(...)) and passes them as separate arguments to print().
# A = 1, 2
# B = 3, 4
#
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]