
sentence = input("Enter a sentence: ")

# Remove spaces and convert to lowercase (optional)
filtered_sentence = sentence.replace(" ", "").lower()

print(filtered_sentence)

from collections import Counter

char_count = Counter(filtered_sentence) # key valua pairs

print(char_count)

for x,y in char_count.items():
    if y>1:
        print (f'{x} -- {y} times')
