#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

# Sample Input
#
# HACK 2
# Sample Output
#
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement

s, k = input().split()
s = sorted(s)  # Sort the string to ensure lexicographical order
k = int(k)

combinations = combinations_with_replacement(s, k)

for combo in combinations:
    print("".join(combo))