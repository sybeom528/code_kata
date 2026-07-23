# 섬 연결하기
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 알고리즘: 그래프, MST
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 20:04:36

def solution(n, costs):
    
    costs.sort(key = lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    answer = 0
    
    def find(a):
        if a != parent[a]:
            parent[a] = find(parent[a])
        return parent[a]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    for start, end, cost in costs:
        if find(start) != find(end):
            union(start, end)
            answer += cost
        
    return answer