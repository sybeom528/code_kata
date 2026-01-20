# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:07:14

def solution(n):
    answer = 1
    
    while (answer * 6) % n != 0:
        answer += 1
    
    return answer