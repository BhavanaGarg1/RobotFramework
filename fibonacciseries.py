import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Example usage
num = int(input("Enter a number: "))

if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is NOT a Fibonacci number.")
