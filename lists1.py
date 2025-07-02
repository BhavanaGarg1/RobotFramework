if __name__ == '__main__':
    x = int(input("Num 1 : "))
    y = int(input("Num 2 : "))
    z = int(input("Num 3 : "))
    n = int(input("Num 4 : "))

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)

# List comprehension