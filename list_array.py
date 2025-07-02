if __name__ == '__main__':
    n = int(input("num1 :"))
    arr = list(map(int, input("num :").split()))
    arr.sort(reverse=True)

    largest = arr[0]
    for ele in arr[1:]:
        if ele < largest:
            print(ele)
            break