if __name__ == '__main__':
    name_list = []
    score_list = []
    records = []
    for _ in range(int(input("num : "))):
        name = input("Name : ")
        score = float(input("Grade : "))
        records.append([name, score])
        name_list.append(name)
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    # print(records)
    # print(score_list)
    second_low = score_list[1]
    # print(second_low)
    out = [i[0] for i in records if i[1] == second_low]
    out.sort()
    for i in out:
        print(i)

# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry