# 순위
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 알고리즘: 그래프, 플로이드워셜
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 19:58:02

def solution(n, results):
    answer = 0
    
    win_lose = [[set() for _ in range(2)] for _ in range(n + 1)]
    
    for i,j in results:
        win_lose[i][1].add(j)
        win_lose[j][0].add(i)
    
    for i in range(1, n + 1):
        for j in win_lose[i][0]:
            win_lose[j][1].update(win_lose[i][1])
        for k in win_lose[i][1]:
            win_lose[k][0].update(win_lose[i][0])
            
    for i in range(1, n + 1):
        if len(win_lose[i][0]) + len(win_lose[i][1]) == n - 1:
            answer += 1
    
    return answer
















# def solution(n, results):
#     answer = 0
    
#     result_list = [[set() for _ in range(2)] for _ in range(n + 1)]
#     rank = [0 for _ in range(n + 1)]
    

#     for i,j in results:
#         result_list[i][1].add(j)
#         result_list[j][0].add(i)
        
#     for k in range(1, n + 1):
#         for i in result_list[k][0]:
#             result_list[i][1].update(result_list[k][1])
#         for j in result_list[k][1]:
#             result_list[j][0].update(result_list[k][0])
        
#     for i in range(1, n + 1):
#         if len(result_list[i][0]) + len(result_list[i][1]) == n - 1:
#             rank[i] = len(result_list[i][0]) + 1
#             answer += 1
                
    
#     return answer