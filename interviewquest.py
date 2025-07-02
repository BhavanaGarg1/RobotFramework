#  s1 = ['A','B','C','D','E','t','Z']
#  s2 = ['c','d','e','f']
#
# Output as [a,C,b,D,c,E,d,F,e,t,z]  python program

s1 = ['A','B','C','D','E','t','Z']
s2 = ['c','d','e','f']

result = []

# Interleave and alternate case
for i in range(len(s2)):
    result.append(s1[i].lower())  # s1 to lowercase
    result.append(s2[i].upper())  # s2 to uppercase

# Add remaining elements from s1 (from i+1 to end), lowercased
for i in range(len(s2), len(s1)):
    result.append(s1[i].lower())

print(result)
