from collections import Counter

def vowel_count(sentence):
    vowel = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowel:
            count += 1
    return count

text = input("Enter your sentence : ")

result = vowel_count(text)
print(f"number of vowels in your sentence is : {result}")