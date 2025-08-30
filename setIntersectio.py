n = int(input())
english_subs = set(map(int, input().split()))
m = int(input())
french_subs = set(map(int, input().split()))

both_subs = english_subs.intersection(french_subs)
print(len(both_subs))

# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
#
# 5