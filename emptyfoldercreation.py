import os
os.makedirs("screenshots", exist_ok=True)

#9.How to enter dynamic id for employees in python without any loop

#list comprehension

emp_id = ['EMP_ID' + str(i) for i in range(1,6)]
print(emp_id)


names = ['Alice', 'Bob', 'Charlie']

employee_id = dict(zip(names,[f'EMP{i}' for i in range(1,len(names) + 1)]))

print(employee_id)

