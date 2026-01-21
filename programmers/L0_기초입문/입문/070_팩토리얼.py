# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:50:54

def solution(n):
    cnt = 1
    num = 1
    while num * (cnt + 1) <= n:
        cnt += 1
        num *= cnt
        
    return cnt