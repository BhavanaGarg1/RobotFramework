#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

# Sample Input
#
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output
#
# 1 2

from collections import deque

d = deque()

for _ in range(int(input())):
    parts = input().split()
    command = parts[0]
    args = parts[1:]

    # Use getattr to dynamically call the method
    if args:
        getattr(d, command)(*map(int, args))
    else:
        getattr(d, command)()

# Print the final deque space-separated
print(*d)
