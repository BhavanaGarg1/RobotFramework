def coptain_room(rooms, k):
	myset = set(rooms)
	ans = (sum(myset)*k) - sum(rooms)
	return (ans // (k-1))


if __name__ == '__main__':
	k = int( input() )
	rooms = list(map(int, input().split()))
	print(coptain_room(rooms, k))


#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
#Sample Input

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# Sample Output
#
# 8