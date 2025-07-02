a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    width = size * 2 - 1
    width += width - 1
    for i in reversed(range(1, size + 1)):
        line = [chr(i + 96)]
        for j in range(i + 1, size + 1):
            line.append(chr(j + 96))
            line.insert(0, chr(j + 96))
        line = "-".join(line)
        print(line.center(width, "-"))

    for i in range(2, size + 1):  # Changed range to avoid repeating the middle row
        line = [chr(i + 96)]
        for j in range(i + 1, size + 1):
            line.append(chr(j + 96))
            line.insert(0, chr(j + 96))
        line = "-".join(line)
        print(line.center(width, "-"))

if __name__ == '__main__':
    n = int(input("Enter size: "))
    print_rangoli(n)




