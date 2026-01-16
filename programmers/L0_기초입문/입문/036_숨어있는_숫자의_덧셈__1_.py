# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 17:47:27

def solution(my_string):
    return sum([int(s) for s in my_string if s.isdigit()])