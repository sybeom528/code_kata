# 백준 문제 1753
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1753
# 작성자: 서윤범
# 작성일: 2026. 02. 24. 09:43:44

import sys
import heapq
input = sys.stdin.readline

V,E = map(int, input().split())

K = int(input())

A = [[] for _ in range(V + 1)]

distance = [sys.maxsize for _ in range(V + 1)]
distance[K] = 0

visited = [False for _ in range(V + 1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    A[u].append([v,w])

hq = []
heapq.heappush(hq, (0,K))

while len(hq) > 0:
    d, now = heapq.heappop(hq)
    if visited[now]:
        continue
    visited[now] = True
    for next, next_d in A[now]:
        if distance[next] > d + next_d:
            distance[next] = d + next_d
            heapq.heappush(hq, (distance[next], next))

for i in range(1,len(distance)):
    if distance[i] == sys.maxsize:
        print('INF')
    else:
        print(distance[i])