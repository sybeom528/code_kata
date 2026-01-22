# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 11:06:09

import math

def solution(n):
    answer = []
    mod = 2
    
    while n >= mod:
        if n % mod == 0:
            answer.append(mod)
            while n % mod == 0:
                n = n // mod
        mod += 1
    
    return answer