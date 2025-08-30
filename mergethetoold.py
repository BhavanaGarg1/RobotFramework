def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
        print("".join(unique_chars))

if __name__ == '__main__':
    string, k = input("Enter string :"), int(input("Enter k value :"))
    merge_the_tools(string, k)

# AABCAAADA
# 3