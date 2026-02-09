# 백준 문제 1253
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1253
# 작성자: 서윤범
# 작성일: 2026. 02. 09. 11:46:14

N = int(input())

A = list(map(int, input().split()))

A.sort()
answer = 0

for k in range(N):
    i = 0
    j = len(A) - 1
    num = A[k]
    while i < j:
        if A[i] + A[j] == num:
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < num:
            i += 1
        else:
            j -= 1
        

print(answer)