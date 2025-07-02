# s = "[This is the [1] test case]"
#
# #output: This is the [1] test case
#
# new = s.strip('[]')
# print(new)
import os

def solve(s):
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)

if __name__ == '__main__':
    s = input("Enter name :")
    result = solve(s)
    print(result)
