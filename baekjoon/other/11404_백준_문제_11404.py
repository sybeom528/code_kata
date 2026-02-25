# 백준 문제 11404
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/11404
# 작성자: 서윤범
# 작성일: 2026. 02. 25. 10:33:17

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

mat = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    if mat[a][b] > c:
        mat[a][b] = c

for i in range(1,N + 1):
    mat[i][i] = 0

for k in range(1, N + 1):
    for i in range(1,N + 1):
        for j in range(1, N + 1):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if mat[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(mat[i][j], end = ' ')
    print()