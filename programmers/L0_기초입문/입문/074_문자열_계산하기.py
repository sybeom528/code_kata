# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 11:14:00

def solution(my_string):
    
    answer = 0
    sign = 1
    
    for s in my_string.split():
        if s.isdigit():
            answer += (int(s) * sign)
        elif s == '+':
            sign = 1
        elif s == '-':
            sign = -1
    
    return answer