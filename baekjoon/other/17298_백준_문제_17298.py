# 백준 문제 17298
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/17298
# 작성자: 서윤범
# 작성일: 2026. 02. 10. 10:32:07

N = int(input())

A = list(map(int, input().split()))

NGE = [-1] * N
stack = []

for i in range(N-1, -1, -1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack:
        NGE[i] = stack[-1]
    
    stack.append(A[i])

for num in NGE:
    print(num, end = ' ')