# Input:numbers_string = "4,2,4,3,2,4,1,3,2"
# Output:[(4, 3), (2, 3), (3, 2), (1, 1)]

input = [1, 3, 1, 3, 2, 2, 3, 1, 3]


def char_freq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


result = char_freq(input)
print(result)

result1 = dict(sorted(result.items(),key= lambda x : x[1],reverse=True))
for char,count in result1.items():
    print(f'{char} is repeated {count} times')






