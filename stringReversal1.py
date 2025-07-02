# s = "I Love Java Programming"
# "I Love Java gnimmargorP"
def reverse_last_word(sentence):
    words = sentence.split()
    if not words:
        return ""

    # Reverse the last word
    words[-1] = words[-1][::-1]

    # Reconstruct the sentence
    return ' '.join(words)


# Test the function
input_str = "I Love Java Programming"
output = reverse_last_word(input_str)
print("Output:", output)

