# 백준 문제 11657
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/11657
# 작성자: 서윤범
# 작성일: 2026. 02. 25. 10:02:40

import sys

N,M = map(int ,input().split())

distance = [sys.maxsize for _ in range(N + 1)]
edge_list = []
distance[1] = 0

for _ in range(M):
    a,b,c = map(int, input().split())
    edge_list.append([a,b,c])

for _ in range(N - 1):
    for a,b,c in edge_list:
        if distance[a] != sys.maxsize and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c

chk_cycle = False
for a,b,c in edge_list:
    if distance[a] != sys.maxsize and distance[b] > distance[a] + c:
        chk_cycle = True
        break

if chk_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])