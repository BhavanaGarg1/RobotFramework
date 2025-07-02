if __name__ == '__main__':
    N = int(input("Enter number : "))
    l1 = []
    for _ in range(N):
        cmd = map(str,input("operation : ").split())
        # print(cmd)
        command = list(cmd)
        # print(cmd_list)
        if command[0] == 'insert':
            l1.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(l1)
        elif command[0] == 'remove':
            l1.remove(int(command[1]))
        elif command[0] == 'append':
            l1.append(int(command[1]))
        elif command[0] == 'sort':
            l1.sort()
        elif command[0] == 'pop':
            l1.pop()
        elif command[0] == 'reverse':
            l1.reverse()
print(l1)

# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]