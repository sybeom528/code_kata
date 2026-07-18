# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 서윤범
# 작성일: 2026. 07. 18. 14:37:20

# def solution(numbers, target):
#     answer = 0
#     n = len(numbers)
    
#     def DFS(i, total):
#         if i == n:
#             if total == target:
#                 return 1
#             else:
#                 return 0
        
#         result = 0
#         result += DFS(i + 1, total + numbers[i])
#         result += DFS(i + 1, total - numbers[i])
#         return result
    
#     return DFS(0,0)

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    
    queue.append([0, numbers[0]])
    queue.append([0, -numbers[0]])
    
    while queue:
        idx, total = queue.popleft()
        if idx == n - 1:
            if total == target:
                answer += 1
        else:
            queue.append([idx + 1, total + numbers[idx + 1]])    
            queue.append([idx + 1, total - numbers[idx + 1]])    
        
    
    return answer