from itertools import permutations
str1, int1 = input("Enter string & num of combination needed : ").split()
print(str1)
print(int1)

for i in sorted(permutations(str1, int(int1))):
    print (''.join(i))