def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


#2nd approach:

from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

print(is_anagram("Listen", "Silent"))  # True
print(is_anagram("Hello", "World"))    # False


# without using built in function

def is_anagram(str1, str2):
    # Step 1: Check length first
    if len(str1) != len(str2):
        return False

    # Step 2: Convert both strings to lowercase manually
    def to_lower(s):
        result = ''
        for ch in s:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)  # Convert uppercase to lowercase
            else:
                result += ch
        return result

    str1 = to_lower(str1)
    str2 = to_lower(str2)

    # Step 3: Count characters manually
    def count_chars(s):
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        return count

    count1 = count_chars(str1)
    count2 = count_chars(str2)

    # Step 4: Compare both dictionaries
    return count1 == count2
