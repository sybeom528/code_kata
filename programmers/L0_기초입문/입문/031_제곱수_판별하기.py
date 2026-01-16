# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 13:27:30

import math

def solution(n):
    return 1 if n % math.sqrt(n) == 0 else 2