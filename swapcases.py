def swap_case(s):
    new_s = ""
    for i in s:
        if i.isupper():
            new_s += i.lower()
        else :
            new_s += i.upper()
    return new_s

if __name__ == '__main__':
    s = input(" Enter your string :")
    result = swap_case(s)
    print(result)