# 여행경로
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 알고리즘: DFS, 그래프
# 작성자: 서윤범
# 작성일: 2026. 07. 18. 15:47:46

from collections import deque

def solution(tickets):
    answer = []
    n = len(tickets)
    queue = deque()
    queue.append([['ICN'], []])
    
    tickets.sort()
    
    while queue:
        now, visited = queue.popleft()
        
        if len(visited) == n:
            return now
        
        for i, (s,e) in enumerate(tickets):
            if i not in visited and now[-1] == s:
                temp_v = visited.copy()
                temp_n = now.copy()
                temp_v.append(i)
                temp_n.append(e)
                queue.append([temp_n, temp_v])