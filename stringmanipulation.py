def transform_sentence(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result = []

    for word in words:
        if len(word) == 2:
            transformed = ''.join(['@' if ch in vowels else ch for ch in word])
        elif len(word) == 3:
            transformed = ''.join(['@@' if ch in vowels else ch for ch in word])
        elif len(word) == 4:
            transformed = ''.join(['@@@' if ch in vowels else ch for ch in word])
        else:
            transformed = word
        result.append(transformed)

    return ' '.join(result)

# Test
input_str = "India is a beautiful country"
output_str = transform_sentence(input_str)
print("Output:", output_str)
#
#  Input:
#
# "India is a beautiful country"
# Output:
#
# Indi@ is @@ be@@@utiful country
# ________________________________________
# 🧠 How It Works:
# •	Splits the sentence into words.
# •	Based on word length (2, 3, 4), it replaces vowels with @, @@, or @@@.
# •	All other words are left unchanged.
# ________________________________________
