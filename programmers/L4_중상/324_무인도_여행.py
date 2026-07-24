# 무인도 여행
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 알고리즘: DFS/BFS
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 16:08:20

from collections import deque

def solution(maps):
    
    result = []
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                queue = deque()
                visited[i][j] = True
                queue.append((i,j))
                total = int(maps[i][j])
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] != 'X' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            total += int(maps[next_x][next_y])
                            queue.append((next_x, next_y))
                result.append(total)
                  
    if result:
        return sorted(result)
    return [-1]
    






















# from collections import deque

# def solution(maps):
#     answer = []
#     dx = [0,1,0,-1]
#     dy = [1,0,-1,0]
#     rows = len(maps)
#     cols = len(maps[0])
#     visit = [[False for _ in range(cols)] for _ in range(rows)]
    
#     def BFS(i,j):
#         queue = deque()
#         queue.append((i,j))
#         days = int(maps[i][j])
#         visit[i][j] = True
#         while queue:
#             now_x,now_y = queue.popleft()
#             for i in range(4):
#                 x = now_x + dx[i]
#                 y = now_y + dy[i]
#                 if 0 <= x <= rows-1 and 0 <= y <= cols-1:
#                     if not visit[x][y] and maps[x][y] != 'X':
#                         queue.append((x,y))
#                         visit[x][y] = True
#                         days += int(maps[x][y])
#         return days
    
#     for i in range(rows):
#         for j in range(cols):
#             if not visit[i][j] and maps[i][j] != 'X':
#                 answer.append(BFS(i,j))
    
#     if len(answer) == 0:
#         return [-1]
    
#     return sorted(answer)