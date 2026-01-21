# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:48:41

def solution(n):
    
    cnt = 1
    chk = False
    num = 1
    while not chk:
        num *= cnt
        if n > num:
            cnt += 1
        elif n == num:
            chk = True
        else:
            cnt -= 1
            chk = True
    
    return cnt