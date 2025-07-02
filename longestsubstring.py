# Program to find the longest unique substring in a given string

def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_substr = ""
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1  # move start past the last occurrence

        char_index[s[end]] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substr = s[start:end+1]

    return max_substr

# Test
input_str = "abcabcbb"
print("Longest unique substring:", longest_unique_substring(input_str))
