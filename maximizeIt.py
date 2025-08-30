# Output Format
#
# Output a single integer denoting the value .
#
# Sample Input
#
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output
#
# 206
# Explanation
#
# Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S
# value equal to (5^2 + 9^2 + 10^2) % 1000 = 206

#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product
n,m = [int(x) for x in input("Enter n and m values :").split()]
li = list()
for i in range(n):
    l= list(map(int,input("Enter list values :").split()))[1:]
    li.append(l)
r = map(lambda x : sum(i*i for i in x)%m,product(*li))
print(max(r))