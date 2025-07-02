s = "Deloitte"

new_str = ""

i = 0

while i < len(s):
    if i +1 < len(s) and s[i] =="t" and s[i +1] == "t":
        new_str += "aa"
        i += 2
    else :
        new_str += s[i]
        i +=1
print(new_str)
