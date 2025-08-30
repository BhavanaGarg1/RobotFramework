def strict_superset(A):
	n = int( input() )
	for x in range(0, n):
		sub_set = set(input().split())
		if len(sub_set.difference(A)):
			return False

	return True


if __name__ == '__main__':
	A = set(input().split())
	if strict_superset(A):
		print('True')
	else:
		print('False')

#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Sample Input 0

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0
#
# False