# 아이템 줍기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 18:45:21

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    max_x = 100
    max_y = 100
    
    maps = [[-1 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if ((x == x1) or (x == x2) or (y == y1) or (y == y2)) and maps[x][y] != -2:
                    maps[x][y] = 0
                else:
                    maps[x][y] = -2
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    queue = deque()
    queue.append((characterX * 2, characterY * 2))
    maps[characterX * 2][characterY * 2] = 0
    
    while queue:
        now_x, now_y = queue.popleft()
        if now_x == itemX * 2 and now_y == itemY * 2:
            return maps[now_x][now_y] // 2
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x <= max_x and 0 <= next_y <= max_y and maps[next_x][next_y] == 0:
                maps[next_x][next_y] = maps[now_x][now_y] + 1
                queue.append((next_x, next_y))


















# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
    
#     max_x = 100; max_y = 100
    
#     maps = [[-3 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    
#     for x1, y1, x2, y2 in rectangle:
#         x1 *= 2
#         y1 *= 2
#         x2 *= 2
#         y2 *= 2
#         for x in range(x1, x2 + 1):
#             for y in range(y1, y2 + 1):
#                 if (x != x1 and x != x2 and y != y1 and y != y2):
#                     maps[x][y] = -2
                    
#     for x1, y1, x2, y2 in rectangle:
#         x1 *= 2
#         y1 *= 2
#         x2 *= 2
#         y2 *= 2
#         for x in range(x1, x2 + 1):
#             for y in range(y1, y2 + 1):
#                 if (x == x1 or x == x2 or y == y1 or y == y2) and (maps[x][y] == -3):
#                     maps[x][y] = -1
    
#     queue = deque()
#     queue.append((characterX * 2, characterY * 2))
    
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
    
#     while queue:
#         now_x, now_y = queue.popleft()
#         if now_x == itemX * 2 and now_y == itemY * 2:
#             return (maps[now_x][now_y] + 1) // 2
#         maps[now_x][now_y] += 1
#         for i in range(4):
#             next_x = now_x + dx[i]
#             next_y = now_y + dy[i]
#             if 0 <= next_x <= max_x and 0 <= next_y <= max_y and maps[next_x][next_y] == -1:
#                 queue.append((next_x, next_y))
#                 maps[next_x][next_y] = maps[now_x][now_y]
    
    
#     return -1