# s = input("Enter a string :")
# s = s.lower()
# new_s = s[::-1]
#
# if s == new_s:
#     print(f'"{s}" is a palindrome')

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

word = "Mom"
if is_palindrome(word):
    print(f'{word} is a palindrome')
else :
    print(f'{word} is not a palindrome')
