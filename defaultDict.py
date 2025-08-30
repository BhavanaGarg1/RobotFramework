from collections import defaultdict
input_n, input_m = map(int, input("Enter grpA size, grpB size: ").split())
d = defaultdict(list)
print(d)
for i in range(input_n):
    ans1 = input("Grp A contains: ")
    d[ans1].append(i+1)
for j in range(input_m):
    ans2 = input("Grp B contains: ")
    if ans2 in d:
        print(*d[ans2])
    else:
        print(-1)

# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'