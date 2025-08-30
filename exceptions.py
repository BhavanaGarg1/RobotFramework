for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)

# Sample Input
#
# 3
# 1 0
# 2 $
# 3 1
# Sample Output
#
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true