# Write a Python function that takes a list of dictionaries representing employee data
# with fields employee_id, name, department, and salary.
# The function should return a dictionary where each key is a department and
# the value is the average salary of employees in that department.
# Example Input:
# employees = [
# {"employee_id": 1, "name": "Alice", "department": "HR", "salary": 5000},
# {"employee_id": 2, "name": "Bob", "department": "HR", "salary": 6000},
# {"employee_id": 3, "name": "Charlie", "department": "Engineering", "salary": 7000}
# ]
# Example Output:
# {
# "HR": 5500,
# "Engineering": 7000
# }

from collections import defaultdict

def average_salary_by_department(employees):
    dept_data = defaultdict(lambda: {'total_salary': 0, 'count': 0})

    for emp in employees:
        dept = emp['department']
        salary = emp['salary']
        dept_data[dept]['total_salary'] += salary
        dept_data[dept]['count'] += 1

    # Compute average for each department
    result = {
        dept: dept_data[dept]['total_salary'] // dept_data[dept]['count']
        for dept in dept_data
    }

    return result

employees = [
    {"employee_id": 1, "name": "Alice", "department": "HR", "salary": 5000},
    {"employee_id": 2, "name": "Bob", "department": "HR", "salary": 6000},
    {"employee_id": 3, "name": "Charlie", "department": "Engineering", "salary": 7000}
]

print(average_salary_by_department(employees))
