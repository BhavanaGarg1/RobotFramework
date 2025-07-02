#print country in a seperate characters from multi list
country = [["USA","Newyork"], ["India","Bangalore"], ["china","wuhan"]]
# step 1: convert to dict
# step 2: loop
# step 3: print key ,values
# step 4: loop inside a loop
# step 5: print in seperate characters

my_dict = dict(country)
print(my_dict)

for x,y in my_dict.items():
    print(x,y)
    for s in x:
        print(s)