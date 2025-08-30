
#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

# Sample Input
#
# TESTCASE 01
#
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
# TESTCASE 02
#
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5
# Sample Output
#
# TESTCASE 01
#
# 78.00
# TESTCASE 02
#
# 81.00

from collections import namedtuple
input_ = int(input())
my_fields = input().split()
print(my_fields)
total_marks = 0
for _ in range(input_):
    students = namedtuple('my_student', my_fields)
    print(students)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = students(MARKS, CLASS, NAME, ID)
    print(my_student)
    total_marks += int(my_student.MARKS)
print((total_marks / input_))
