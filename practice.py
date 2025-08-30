def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example
fibonacci_series(10)
