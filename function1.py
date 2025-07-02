def is_leap(year):
    # Leap year if divisible by 4 and (not divisible by 100 unless divisible by 400)
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter a year: "))
print(is_leap(year))