#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict
a = OrderedDict()
input_ = int(input())
for _ in range(input_):
    item, space, price = input().rpartition(' ')
    a[item] = a.get(item, 0) + int(price)
    print(a.items())
for item, price in a.items():
    print(item, price)

# Steps Used in solving the problem -
# Step 1: First, we have imported OrderedDict.
# Step 2: Then, we created two variables. The first one is to store our OrderedDict and
# the second is to take input.
# Step 3: In fourth step we have created a for loop in range of our input.
# Step 4: Then, we used the input method to take input of item, space, and price. We
# have used rpartition method to split our inputs in three parts.
# Step 5: Then, we created another for loop in a.items.
# Step 6: In last step we have printed item and price.

# Sample Input
#
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# Sample Output
#
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20