# 구슬을 나누는 경우의 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 12:20:48

def solution(balls, share):
    
    def fact(n):
        if n == 1 or n == 0:
            return 1
        return n * fact(n-1)
    
    return fact(balls) / ( fact(share) * fact(balls - share))