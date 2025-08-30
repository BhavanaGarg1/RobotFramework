#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

from math import degrees, atan2

AB = float(input())
BC = float(input())

MBC = round(degrees(atan2(AB, BC)))
print((str(MBC)), chr(176), sep='')

# Steps Used in solving the problem -
#
# Step 1:  First we imported degrees and atan2 from math.
# Step 2: then we have taken the input of AB and BC.
# Step 3: After this, we used the atan2 function to calculate the angle MBC. we have used the round method to change our ans in round number.
# Step 4: At last we have returned our ans as a string. Here, we have used char(176) to add the degree symbol.
#
# Sample Input
#
# 10
# 10
# Sample Output
#
# 45°
#
