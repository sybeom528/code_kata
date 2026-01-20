# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:31:04

def solution(my_string):
    unique_string = []
    answer = ''
    
    for s in my_string:
        if s not in unique_string:
            unique_string.append(s)
            answer += s
        else:
            continue
    
    return answer