if __name__ == '__main__':
    # Read the number of elements in the first set (M) and the elements themselves
    M = int(input())
    set_M = set(map(int, input().split()))

    # Read the number of elements in the second set (N) and the elements themselves
    N = int(input())
    set_N = set(map(int, input().split()))

    # Calculate the symmetric difference
    # This can be done using the .symmetric_difference() method or the ^ operator
    symmetric_diff = set_M.symmetric_difference(set_N)
    # Alternatively: symmetric_diff = set_M ^ set_N

    print(len(symmetric_diff))

    # Convert the resulting set to a list, sort it, and print each element
    # for item in sorted(list(symmetric_diff)):
    #     print(item)

#https://codersdaily.in/courses/hacker-rank-solution/symmetric-difference

# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

8

