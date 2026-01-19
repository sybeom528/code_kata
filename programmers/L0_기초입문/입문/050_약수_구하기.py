# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 11:06:06

import math

def solution(n):
    answer = [1,n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer.append(i)
            answer.append(n//i)
    
    return sorted(list(set(answer)))