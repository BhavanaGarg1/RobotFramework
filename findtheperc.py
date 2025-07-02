if __name__ == '__main__':
    n = int(input("Number : "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter values : ").split()
        scores = list(map(float, line))
        print(scores)
        student_marks[name] = scores
    query_name = input("Enter name :")
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f"))

# Input (stdin)
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Your Output (stdout)
# 56.00
# Expected Output
# 56.00

# input("Enter values : ") → gets a string like:
# "Bhavana 78 89 90"
#
# .split() → splits it into a list:
# ['Bhavana', '78', '89', '90']
#
# name, *line = ... uses Python's extended iterable unpacking:
#
# name = 'Bhavana' (the first element)
#
# *line = ['78', '89', '90'] (all the remaining elements go into the line list)
#
# # Input: "Bhavana 78 89 90"
# name = "Bhavana"
# line = ['78', '89', '90']
# map(float, line) → converts every string in line to a float:
#
# ['78', '89', '90'] → [78.0, 89.0, 90.0]
#
# list(...) → wraps the result into a list
# scores = [78.0, 89.0, 90.0]