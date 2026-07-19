# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 서윤범
# 작성일: 2026. 07. 19. 17:45:55

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    
    def DFS(hp, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and hp >= need:
                visited[i] = True
                DFS(hp - cost, cnt + 1)
                visited[i] = False
                
    DFS(k,0)
    
    return answer

# BFS로 구현했지만, 베스트는 DFS + 백트래킹
# from collections import deque

# def solution(k, dungeons):
#     answer = -1
#     n = len(dungeons)
    
#     queue = deque()
#     for i in range(n):
#         if dungeons[i][0] <= k:
#             queue.append([k - dungeons[i][1],[i],1])
    
#     while queue:
#         now_hp, visited, cnt = queue.popleft()
#         final_chk = True
#         for i in range(n):
#             if i not in visited and dungeons[i][0] <= now_hp:
#                 final_chk = False
#                 temp = visited.copy()
#                 temp.append(i)
#                 queue.append((now_hp - dungeons[i][1], temp, cnt + 1))
#         if final_chk:
#             if cnt > answer:
#                 answer = cnt
                
#     return answer