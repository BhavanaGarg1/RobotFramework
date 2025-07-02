students = [
    {"name": "Alice", "age": 20, "grades": [80, 85, 90]},
    {"name": "Bob", "age": 22, "grades": [70, 75, 65]},
    {"name": "Charlie", "age": 19, "grades": [88, 92, 85]},
    {"name": "Diana", "age": 21, "grades": [60, 65, 70]}
]

print("Students with average grade > 80:\n")

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    if avg > 80:
        print(f"Name: {student['name']}, Age: {student['age']}, Average: {avg:.2f}")
