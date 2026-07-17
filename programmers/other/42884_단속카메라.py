# 단속카메라
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 18:27:28

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x: x[1])
    
    now_idx = 0
    for i in range(1, len(routes)):
        if routes[now_idx][1] < routes[i][0]:
            answer += 1
            now_idx = i
    
    return answer + 1