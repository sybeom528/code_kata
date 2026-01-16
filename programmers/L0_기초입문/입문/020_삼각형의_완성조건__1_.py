# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 12:50:18

def solution(sides):
    sides = sorted(sides)
    return 2 if sides[2] >= sides[0] + sides[1] else 1