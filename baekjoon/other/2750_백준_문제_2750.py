# 백준 문제 2750
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/2750
# 작성자: 서윤범
# 작성일: 2026. 02. 19. 11:37:13

N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))

for i in range(N-1):
    for j in range(N-1-i):
        if num[j] > num[j+1]:
            num[j], num[j + 1] = num[j + 1], num[j]

for i in range(N):
    print(num[i])