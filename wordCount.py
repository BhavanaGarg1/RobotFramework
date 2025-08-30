s = "java java not adding string string values any data data"

word = s.split()
print(word)

from collections import Counter

output = Counter(word)
print(output)


for x,y in output.items():
    print(f"{x} is repeated {y} times")



# word_count = {}
#
# for w in word:
#     if w in word_count:
#         word_count[w] += 1
#     else :
#         word_count[w] = 1
#
# print(word_count)
#
# for x,y in word_count.items():
#     print(f"{x} is repeated {y} times")