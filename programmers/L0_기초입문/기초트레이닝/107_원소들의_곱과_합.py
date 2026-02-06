# 원소들의 곱과 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181929
# 알고리즘: 조건문
# 작성자: 서윤범
# 작성일: 2026. 02. 06. 13:42:20

import math

def solution(num_list):
    mult = math.prod(num_list)
    ss = sum(num_list) ** 2
    return 1 if mult < ss else 0