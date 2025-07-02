from itertools import product

input_A = list(map(int, input("Num 1 :").split()))
input_B = list(map(int, input("Num 2 :").split()))

print(*list(product(input_A, input_B)))


# A = 1, 2
# B = 3, 4
#
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]