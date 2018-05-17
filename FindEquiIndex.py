def solution(A, N):
	prefSum = A[0]
	sufSum = A[N-1]
	fwdIndex = 1
	bwdIndex = N-2
	while fwdIndex != bwdIndex:
		if (prefSum < sufSum):
			prefSum = prefSum + A[fwdIndex]
			fwdIndex+=1
		else:
			if (prefSum > sufSum):
				sufSum = sufSum + A[bwdIndex]
				bwdIndex-=1
			else:
				return fwdIndex-1		
	return -1

A = [-1, 3, -4, 5, 1, -6, 2, 1]

print solution(A, 8)


