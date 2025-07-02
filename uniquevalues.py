arr = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Unique values:", unique)
