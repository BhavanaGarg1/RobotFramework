#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)
if not m:
    print("(-1,-1)")
else:
    while m:
        print("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(s, m.start() + 1)

# Sample Input
#
# aaadaa
# aa
# Sample Output
#
# (0, 1)
# (1, 2)
# (4, 5)

# import re
#
# S = input()
# k = input()
#
# pattern = re.compile(f'(?={re.escape(k)})')
# matches = list(pattern.finditer(S))
#
# if matches:
#     for m in matches:
#         print((m.start(), m.start() + len(k) - 1))
# else:
#     print((-1, -1))