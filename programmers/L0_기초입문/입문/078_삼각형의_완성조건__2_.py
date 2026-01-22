# 삼각형의 완성조건 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 12:17:42

def solution(sides):
    sides = sorted(sides)
    # (b + a - 1) + (b - a + 1) + 1 = 2a - 1
    return sides[0] * 2 - 1