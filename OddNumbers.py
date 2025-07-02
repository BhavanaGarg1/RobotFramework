#write a program to enlist odd numbers from input array list

input_array = [1,2,3,4,5,6,7,8,9,10]

def get_odd_numbers(input_list):
    odd_nos = [num for num in input_list if num % 2 != 0]
    return odd_nos

result = get_odd_numbers(input_array)
print(f"Odd numbers in given array are : {result}")
