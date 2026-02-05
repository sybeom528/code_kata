# 분수의 덧셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 11:35:41

def gcd(a,b):
    a,b = max(a,b), min(a,b)
    while b > 0:
        a,b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    num = gcd(denom1, denom2)
    
    denom = denom1 * denom2 / num
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)
    
    num2 = gcd(numer, denom)
    
    return [numer // num2, denom // num2]