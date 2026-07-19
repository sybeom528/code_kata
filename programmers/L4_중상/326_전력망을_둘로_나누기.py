# 전력망을 둘로 나누기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 알고리즘: DFS/BFS, 그래프
# 작성자: 서윤범
# 작성일: 2026. 07. 19. 18:15:07

from collections import deque
import sys

def solution(n, wires):
    answer = sys.maxsize
    
    tree = [[] for _ in range(n + 1)]
    
    for s,e in wires:
        tree[s].append(e)
        tree[e].append(s)
    
    print(tree)
    def BFS(i):
        queue = deque()
        visited = [False] * (n + 1)
        queue.append(i)
        visited[i] = True
        while queue:
            now_node = queue.popleft()
            for next in tree[now_node]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)
        
        return sum(visited)
                
    for s,e in wires: 
        tree[s].remove(e)
        tree[e].remove(s)
        visited = [False] * (n + 1)
        cnt = 0
        result = BFS(1)
        result = abs((n - result) - result)
        answer = min(answer, result)
        tree[s].append(e)
        tree[e].append(s)

    return answer