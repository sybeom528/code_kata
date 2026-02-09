# 백준 문제 11003
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/11003
# 작성자: 서윤범
# 작성일: 2026. 02. 09. 12:19:03

from collections import deque

N, L  = map(int, input().split())

A = list(map(int, input().split()))

queue = deque()

for i in range(N):
    while queue and queue[-1][0] >= A[i]:
        queue.pop()
    queue.append((A[i],i))
    if queue[0][1] <= i - L:
        queue.popleft()
    print(queue[0][0], end = ' ')