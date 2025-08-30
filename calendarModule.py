#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

# Sample Input
#
# 08 05 2015
# Sample Output
#
# WEDNESDAY
# Explanation
#
# The day on 5th August 2015 was WEDNESDAY.

import calendar
month, day, year = list(map(int,input().split()))
ans = calendar.weekday(year, month, day)
print((calendar.day_name[ans]).upper())

# Steps Used in solving the problem -
# Step 1: First we imported the calendar.
# Step 2: In the second step we have taken the input of month, day, and year.
# Step 3: then calendar.weekday to get the weekday of our input.
# Step 4: At last we used the calendar.day_name to get the day name of our weekday.