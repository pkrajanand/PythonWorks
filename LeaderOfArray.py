def solution(A):
     n = len(A)
     L = [-1] + A
     count = 0
     pos = (n + 1) // 2
     candidate = L[pos]
     for i in range(1, n + 1):
         if (L[i] == candidate):
             count = count + 1
     if (count > pos):
         return candidate
     return -1

A = [2,2,2,2,2,2,4,4,4,6,7]

pos = (len(A) + 1) // 2

print pos

print solution(A)