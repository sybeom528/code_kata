# 여행경로
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 알고리즘: DFS, 그래프
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 18:19:38

def solution(tickets):
    
    tickets.sort()
    n = len(tickets)
    visited = [False] * n
    
    def DFS(city):
        if sum(visited) == n:
            return city
        
        for i, (prev, next) in enumerate(tickets):
            if not visited[i] and prev == city[-1]:
                visited[i] = True
                city.append(next)
                result = DFS(city)
                if result:
                    return result
                city.pop()
                visited[i] = False
    
    return DFS(['ICN'])

















# def solution(tickets):
    
#     tickets.sort()
#     n = len(tickets)
#     visited = [False] * n
    
#     def DFS(path):
#         if sum(visited) == n:
#             return path
        
#         for i, (s,e) in enumerate(tickets):
#             if not visited[i] and path[-1] == s:
#                 visited[i] = True
#                 path.append(e)
#                 result = DFS(path)
#                 if result:
#                     return result
#                 visited[i] = False
#                 path.pop()
    
#     return DFS(['ICN'])
    
    

# BFS로 구현하긴 했지만, DFS + 백트래킹이 더 맞는 문제
# from collections import deque

# def solution(tickets):
#     answer = []
#     n = len(tickets)
#     queue = deque()
#     queue.append([['ICN'], []])
    
#     tickets.sort()
    
#     while queue:
#         now, visited = queue.popleft()
        
#         if len(visited) == n:
#             return now
        
#         for i, (s,e) in enumerate(tickets):
#             if i not in visited and now[-1] == s:
#                 temp_v = visited.copy()
#                 temp_n = now.copy()
#                 temp_v.append(i)
#                 temp_n.append(e)
#                 queue.append([temp_n, temp_v])