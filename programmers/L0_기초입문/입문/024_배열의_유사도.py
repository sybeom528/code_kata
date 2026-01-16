# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 13:04:07

def solution(s1, s2):
    return sum([1 if s in s2 else 0 for s in s1])