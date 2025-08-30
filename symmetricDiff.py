#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

n1 = int(input())
set_a = set(map(int,input().split()))
n2 = int(input())
set_b = set(map(int,input().split()))
a = (set_a.difference(set_b))
b = (set_b.difference(set_a))
ans = a.union(b)
for i in sorted(ans):
        print (i)

# Steps used in solving the problem -
#
# Step 1:  First we have taken the input of n1 and set_a.
# Step 2: Similarly, we have taken the input of n2 and set_b.
# Step 3: then we used a for loop in elements_arr.
# Step 4: then we used the difference method to find the number which exist in set_a but not in set_b. We have done the same thing with set_b and stored both values in a and b.
# Step 5: after this, we used the union method to find the values which exist in a or b.
# Step 6: In last step we used a for loop in our sorted answer and then we printed each value.

# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.
#
# Sample Input
#
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output
#
# 5
# 9
# 11
# 12