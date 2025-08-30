


# with open("C:\\Users\\dinesh garg\\PycharmProjects\\DataAutomation\\name.txt","a") as f:
#     new=f.write("Kathi")


with open("C:\\Users\\dinesh garg\\PycharmProjects\\DataAutomation\\name.txt","r") as f:
    new=f.read()
    print(new)
    s = new.replace("Bhavana","Urmila")

with open("C:\\Users\\dinesh garg\\PycharmProjects\\DataAutomation\\name.txt","w") as f:
    f.write(s)





