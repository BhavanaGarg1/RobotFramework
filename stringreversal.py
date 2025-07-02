s = "Automation Testing"
new_s = s.split()
print(new_s)

# new_s = new_s[::-1]
# print(new_s)

reversed_string = ' '.join(s[::-1] for s in new_s)
print(reversed_string)