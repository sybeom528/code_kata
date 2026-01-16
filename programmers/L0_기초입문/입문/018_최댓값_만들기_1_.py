# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 12:39:03

def solution(numbers):
    tmp = sorted(numbers, reverse = True)[:2]
    return tmp[0] * tmp[1]