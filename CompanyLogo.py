#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input("Enter your string :")
    z = Counter(s)
    print(z)
    z = Counter(s).most_common(3)
    print(z)
    for x in z:
        print(*x)


# Output Format
#
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
#
# Sample Input 0
#
# aabbbccde
# Sample Output 0
#
# b 3
# a 2
# c 2