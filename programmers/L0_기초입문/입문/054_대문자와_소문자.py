# 대문자와 소문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:03:35

def solution(my_string):
    answer = ''
    for s in my_string:
        if s.islower():
            answer += s.upper()
        else:
            answer += s.lower()
    return answer