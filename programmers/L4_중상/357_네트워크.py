# 네트워크
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 알고리즘: DFS/BFS
# 작성자: 서윤범
# 작성일: 2026. 07. 18. 14:47:11

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def DFS(i):
        visited[i] = True
        for j in range(n):
            if i == j:
                continue
            elif not visited[j] and computers[i][j] == 1:
                DFS(j)
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    
    return answer