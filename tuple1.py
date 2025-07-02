if __name__ == '__main__':
    n = int(input('Enter num : '))
    integer_list = map(int, input("Enter tuple element : ").split())
    t = tuple(integer_list)
    print(hash(t))