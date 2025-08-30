def is_palindrome(s):
    return s == s[::-1]

def find_all_palindromes(word):
    word = word.lower()  # Optional: ignore case
    n = len(word)
    palindromes = set()

    for i in range(n):
        for j in range(i + 2, n + 1):  # substrings of length ≥ 2
            sub = word[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)

    return palindromes

# Input string
word = "Bhavananan"

# Find palindromes
palindromes = find_all_palindromes(word)

print("✅ Palindromic substrings found:", palindromes)

# Get smallest palindrome(s)
if palindromes:
    min_len = min(len(p) for p in palindromes)
    smallest = [p for p in palindromes if len(p) == min_len]
    print("✅ Smallest palindrome(s):", smallest)
else:
    print("❌ No palindromes found.")
