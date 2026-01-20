# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:25:22

def solution(order):
    return sum([1 if s in ['3','6','9'] else 0 for s in str(order)])