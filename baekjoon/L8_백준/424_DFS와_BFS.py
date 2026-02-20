# DFS와 BFS
# 백준 레벨8 (백준)
# 문제 링크: https://www.acmicpc.net/problem/1260
# 알고리즘: DFS/BFS
# 작성자: 서윤범
# 작성일: 2026. 02. 20. 10:58:28

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N,M,V = map(int, input().split())

A = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(1,N + 1):
    A[i].sort()

visited = [False for _ in range(N + 1)]

def DFS(i):
    visited[i] = True
    print(i, end = ' ')
    for j in A[i]:
        if not visited[j]:
            DFS(j)

DFS(V)
print()

visited = [False for _ in range(N + 1)]

def BFS(i):
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for next in A[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

BFS(V)