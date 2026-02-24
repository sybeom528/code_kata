# 백준 문제 1854
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1854
# 작성자: 서윤범
# 작성일: 2026. 02. 24. 11:00:18

import sys
import heapq
input = sys.stdin.readline

n,m,k = map(int, input().split())

A = [[] for _ in range(n + 1)]
distance = [[sys.maxsize for _ in range(k)] for _ in range(n + 1)]
distance[1][0] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    A[a].append([b,c])

hq = []
heapq.heappush(hq, (0,1))

while len(hq) > 0:
    now_dist, now_node = heapq.heappop(hq)
    for next_node, next_dist in A[now_node]:
        # 마지막 것만 비교하고, sort하면 해결
        if distance[next_node][k-1] > now_dist + next_dist:
            distance[next_node][k-1] = now_dist + next_dist
            distance[next_node].sort()
            heapq.heappush(hq,(now_dist + next_dist, next_node))

for i in range(1, len(distance)):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])