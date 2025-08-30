#Find out the sum of two number is equal to 6, from an array of number (1, 2, 3, 2, 3, 4)

arr = [1, 2, 3, 2, 3, 4]
target = 6
seen = set()
result = set()

for num in arr:
    complement = target - num
    if complement in seen:
        result.add(tuple(sorted((num, complement))))
        print(result)
    seen.add(num)

for pair in result:
    print(f"Pair: {pair}")

