# 게임 맵 최단거리
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 작성자: 서윤범
# 작성일: 2026. 07. 18. 16:19:03

from collections import deque

def solution(maps):
    
    n = len(maps); m = len(maps[0])
    
    queue = deque()
    maps[0][0] = 1
    queue.append((0,0))
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while queue:
        x,y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1:
                maps[next_x][next_y] = maps[x][y] + 1
                queue.append((next_x, next_y))
                
    return -1