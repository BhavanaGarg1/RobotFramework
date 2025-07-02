# Enter number of rows: 5
# 1
# 12
# 123
# 1234
# 12345

n = int(input("Enter num of rows : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


# reverse pattern
m = int(input("Enter num of rows : "))

for i in range(m,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#Alphabets

o = int(input("Enter num of rows : "))

for i in range(1,o+1):
    for j in range(i):
        print(chr(65 +j),end="") # 65 = ASCII for 'A'
    print()


# reverse alpha pattern
p = int(input("Enter num of rows : "))

for i in range(p,0,-1):
    for j in range(i):
        print(chr(65 + j),end="") # 65 = ASCII for 'A'
    print()

#right alignment

q = int(input("Enter number of rows: "))

for i in range(1, q + 1):
    print(" " * (q - i), end="")  # leading spaces for right alignment
    for j in range(i):
        print(chr(65 + j), end="")
    print()

