n = int(input())
english_subscriptions = set(map(int, input().split()))
m = int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.union(french_subscriptions)
print(len(all_subscriptions))

# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
#
# 13