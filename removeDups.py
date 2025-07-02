input_str = "programming"

def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

output = remove_duplicates(input_str)

print(f"Input string : {input_str}")
print(f"Output string {output}")