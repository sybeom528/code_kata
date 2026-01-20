# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:10:16

def solution(age):
    
    answer = ''
    
    for s in str(age):
        answer += chr(ord('a') + int(s))

    return answer