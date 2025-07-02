
def split_and_join(line):
    # write your code here
    l1 = line.split(" ")
    line = "-".join(l1)
    return line


if __name__ == '__main__':
    line = input("Enter your string : ")
    result = split_and_join(line)
    print(result)