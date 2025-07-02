#avg. of tress height

def average(arr):
    this_set = set(arr)
    avg = sum(this_set)/len(this_set)
    return avg

if __name__ == '__main__':
    n= int(input("Enter num of trees :"))
    tree_height_array = list(map(int,input("Enter height of the tress :").split()))
    result = average(tree_height_array)
    print(result)

# 10
# 161 182 161 154 176 170 167 171 170 174