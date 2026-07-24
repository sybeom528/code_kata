# 리코쳇 로봇
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 알고리즘: BFS
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 15:45:07

from collections import deque

def solution(board):
    
    n = len(board)
    m = len(board[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i,j
            elif board[i][j] == 'G':
                end_x, end_y = i,j
    
    visited[start_x][start_y] = True
    
    queue = deque()
    queue.append((start_x,start_y,0))
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while queue:
        x,y,cnt = queue.popleft()
        if board[x][y] == 'G':
            return cnt
        
        for i in range(4):
            next_x = x
            next_y = y
            while 0 <= next_x + dx[i] < n and 0 <= next_y + dy[i] < m and board[next_x + dx[i]][next_y + dy[i]] != 'D':
                    next_x += dx[i]
                    next_y += dy[i]
            
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, cnt + 1))
    
    return -1























## 내 풀이
# from collections import deque

# def solution(board):
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     board_list = []
#     for i in range(len(board)):
#         board_list.append([])
#         for j in board[i]:
#             board_list[i].append(j)
#             if j == 'R':
#                 start_x,start_y = i,len(board_list[i])-1
#                 board_list[start_x][start_y] = '0'
#             elif j == 'G':
#                 end_x,end_y = i,len(board_list[i])-1
#     queue = deque()
#     cnt = 0
#     queue.append((start_x,start_y,cnt))
#     answer = 0
#     while queue and answer == 0:
#         now_x, now_y,cnt = queue.popleft()
#         for d in range(4):
#             x = dx[d]
#             y = dy[d]
#             move_x,move_y = now_x,now_y
#             # 멈출때까지 이동
#             while 0 <= move_x <= len(board_list) - 1 and 0 <= move_y <= len(board_list[0]) - 1:
#                 move_x = move_x + x; move_y = move_y + y
#                 if move_x < 0 or move_y < 0 or move_x > len(board_list)-1 or move_y > len(board_list[0]) - 1:
#                     move_x = move_x - x; move_y = move_y - y
#                     break
#                 elif board_list[move_x][move_y] == 'D':
#                     move_x = move_x - x; move_y = move_y - y
#                     break
#             # 방문하지 않은 곳이면 queue에 append
#             if board_list[move_x][move_y] == '.':
#                 board_list[move_x][move_y] = str(cnt+1)
#                 queue.append((move_x,move_y,cnt+1))
#             # 방문한 경우에 이동거리가 더 짧으면 append
#             elif board_list[move_x][move_y].isdigit():
#                 if cnt+1 < int(board_list[move_x][move_y]):
#                     board_list[move_x][move_y] = str(cnt+1)
#                     queue.append((move_x,move_y,cnt+1))
#             # 도착한 경우면
#             elif board_list[move_x][move_y] == 'G':
#                 answer = cnt+1
#                 break
    
#     if answer == 0:
#         return -1
#     else:
#         return answer

## 수정한 풀이

# from collections import deque

# def solution(board):
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     lenR,lenC = len(board), len(board[0])
#     visit = [[-1 for _ in range(lenC)] for _ in range(lenR)]
#     for i in range(lenR):
#         for j in range(lenC):
#             if board[i][j] == 'R':
#                 start_x,start_y = i,j
#                 break
    
#     queue = deque()
#     cnt = 0
#     queue.append((start_x,start_y,cnt))
#     answer = 0
#     while queue and answer == 0:
#         now_x, now_y,cnt = queue.popleft()
#         for d in range(4):
#             x = dx[d]
#             y = dy[d]
#             move_x,move_y = now_x,now_y
#             # 멈출때까지 이동
#             while True:
#                 move_x += x; move_y += y
#                 if move_x < 0 or move_y < 0 or move_x > lenR-1 or move_y > lenC-1:
#                     break
#                 elif board[move_x][move_y] == 'D':
#                     break
#             move_x -= x; move_y -= y
#             # 방문한 경우에 이동거리가 더 짧으면 append
#             if visit[move_x][move_y] > 0:
#                 if cnt+1 < visit[move_x][move_y]:
#                     visit[move_x][move_y] = cnt + 1
#                     queue.append((move_x,move_y,cnt+1))
#             # 도착했으면
#             elif board[move_x][move_y] == 'G':
#                 answer = cnt + 1
#                 break
#             # 이동
#             else:
#                 visit[move_x][move_y] = cnt+1
#                 queue.append((move_x,move_y,cnt+1))
    
#     if answer == 0:
#         return -1
#     else:
#         return answer