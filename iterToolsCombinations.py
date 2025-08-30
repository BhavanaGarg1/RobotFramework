#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

# Sample Input
#
# HACK 2
# Sample Output
#
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK


from itertools import combinations
word , length  = input().split()
for i in range(1, int(length)+1):
    for j in combinations(sorted(word), i):
        print (''.join(j))


# Steps used in solving the problem -
# Step 1: First we imported combinations from itertools.
# Step 2: then, we have taken the input of word and length.
# Step 3: After this, we created a for loop in the range of 1 to (length+1).
# Step 4: Inside for loop, we created another for loop and used the "combinations" method to make combinations and the "sorted" method to sort these combinations alphabetically.
# Step 5: In the last step, we used the join method and printed our combinations.