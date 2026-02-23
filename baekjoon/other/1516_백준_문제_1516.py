# 백준 문제 1516
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1516
# 작성자: 서윤범
# 작성일: 2026. 02. 23. 11:49:27

from collections import deque

N = int(input())

build_info = [[] for _ in range(N + 1)]
orders = [1 for _ in range(N + 1)]
build_time = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    info = list(map(int, input().split()))
    build_time[i] = info[0]
    for build in info[1:-1]:
        build_info[build].append(i)
        orders[i] += 1

queue = deque()

for i in range(1,N + 1):
    if orders[i] == 1:
        queue.append(i)

while queue:
    now_build = queue.popleft()
    result[now_build] += build_time[now_build]
    orders[now_build] -= 1
    for next in build_info[now_build]:
        orders[next] -= 1
        if orders[next] == 1:
            queue.append(next)
        result[next] = max(result[next], result[now_build])
    
for i in range(1,N + 1):
    print(result[i])