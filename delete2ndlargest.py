arr = [5, 1, 9, 6, 9, 2]

unique_num = set(arr)
print(unique_num)

unique_num_list = list(unique_num)
unique_num_list.sort(reverse=True)
print(unique_num_list)

second_largest = unique_num_list[1]
print(second_largest)

unique_num_list.pop(1)
print(unique_num_list)
#
# unique_num_list.remove(second_largest)
# print(unique_num_list)