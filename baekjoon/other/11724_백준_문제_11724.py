# 백준 문제 11724
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/11724
# 작성자: 서윤범
# 작성일: 2026. 02. 20. 10:49:34

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int, input().split())

A = [[] for _ in range(N + 1)]

for _ in range(M):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

visited = [False for _ in range(N + 1)]

def DFS(i):
    visited[i] = True
    for j in A[i]:
        if not visited[j]:
            DFS(j)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)

