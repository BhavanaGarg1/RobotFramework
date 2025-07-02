def mutate_string(string, position, character):
    split_str = list(string)
    split_str[position] = character
    string = "".join(split_str)
    return string

if __name__ == '__main__':
    s = input("Enter string : ")
    i, c = input("position,char :").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character