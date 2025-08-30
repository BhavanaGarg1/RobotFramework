# [1,3,1,3,2,2,3,1,3] is a list. print the count of each integer and descending order
# without using collections or any other inbuilt libraries

nums = [1, 3, 1, 3, 2, 2, 3, 1, 3]

# Step 1: Count occurrences using a dictionary
count_dict = {}
for num in nums:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Step 2: Convert dictionary to list of tuples (num, count)
count_list = []
for key in count_dict:
    count_list.append((key, count_dict[key]))

print(count_list)

print(len(count_list))

# Step 3: Sort the list in descending order of count
for i in range(len(count_list)):
    for j in range(i + 1, len(count_list)):
        if count_list[i][1] < count_list[j][1]:
            count_list[i], count_list[j] = count_list[j], count_list[i]

# Step 4: Print the counts
for item in count_list:
    print(f"{item[0]} -> {item[1]}")


# second approach
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