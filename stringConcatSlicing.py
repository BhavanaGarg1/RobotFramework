def string_concat(s):
    start = s[:2]
    print(start)
    end = s[-3:]
    print(end)
    return start + end

result = input("enter string :")
print(string_concat(result))

