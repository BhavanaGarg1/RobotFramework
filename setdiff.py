#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
#
# 4
# Explanation
#
# The roll numbers of students who only have English newspaper subscriptions are:
# 4,5,7 and 9.
# Hence, the total is 4 students.

n=input()
e=set(input().split())
b=input()
f=set(input().split())
print(len(e-f))