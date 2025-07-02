

input_str = input("Enter your string : ")

from collections import Counter

new_str = input_str.lower()

char_count = Counter(new_str)

for x,y in char_count.items():
    if y>1:
        print(f"{x} repeated {y} times")