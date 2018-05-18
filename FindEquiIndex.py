def solution(A):
	N = len(A)

	if (N == 1):
		return 0
	if (N == 0):
		return -1

	i = 1
	while ( i < N):
		prefSum = sumIt(A, 0, i-1)
		sufSum = sumIt(A, i+1, N-1)
		if (prefSum == sufSum):
			return  i
		i += 1

	return -1

def sumIt(A, start, end):
	j = start
	sumNum = 0
	while (j <= end):
		sumNum += A[j]
		j += 1

	return sumNum


A = [5,6]
s = solution(A)
print '%s: %d'  % (str(A), s)

A = [0, -1, -1]
s = solution(A)
print '%s: %d'  % (str(A), s)

A = [-1, 3, -4, 5, 1, -6, 2, 1]
s = solution(A)
print '%s: %d'  % (str(A), s)

A = [5,6,5]
s = solution(A)
print '%s: %d'  % (str(A), s)

A = [2,3,5,2,1,2]
s = solution(A)
print '%s: %d'  % (str(A), s)
