def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_substring = ""
    seen = {}

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # move start forward to skip the duplicate
        seen[char] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substring = s[start:end+1]

    return max_substring

# Example usage:
input_str = "abcabcbb"
result = longest_unique_substring(input_str)
print(f"Longest unique substring in '{input_str}' is: '{result}'")
# ________________________________________
# 🧠 How It Works:
# •	start: Beginning of current window
# •	seen: Dictionary to store the last index of each character
# •	If a character repeats within the current window, we slide the window forward.
# ________________________________________
