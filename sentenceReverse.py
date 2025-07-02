#	Print Hello World as olleH dlroW

input_str = "Hello World"

reversed_words = ' '.join(word[::-1] for word in input_str.split())

print(reversed_words)
