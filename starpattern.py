a = 0
increasing = True

while True:
    print("*" * a)

    if increasing:
        a += 1
        if a > 5:
            a -= 2
            increasing = False
    else:
        if a <= 0:
            break
        a -= 1


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

