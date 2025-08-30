#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())
Country = set()
for i in range(n):
    Country.add(input())
print(len(Country))

# Sample Input
#
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Sample Output
#
# 5
