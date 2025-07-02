array = [16, 17, 4, 3, 5, 2]
# •	Start from the rightmost element (always a leader)
# •	Keep track of the current maximum on the right
# •	If current element > max_right → it's a leader

def find_leader(arr):
    leader = []
    fixedldr = array[-1]
    leader.append(fixedldr)

    for i in range(len(arr) -2,-1,-1):
        if arr[i] > fixedldr:
            fixedldr = arr[i]
            leader.append(fixedldr)
    return leader[::-1]

print("Leaders are :", find_leader(array))


