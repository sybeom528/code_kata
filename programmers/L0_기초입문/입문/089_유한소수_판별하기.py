# 유한소수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120878
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 21:39:37

def solution(a, b):
    answer = 0
    
    # 최대공약수 함수
    def gcd(a,b):
        while b > 0:
            a,b = b, a % b
        return a
    
    num = gcd(a,b)
    
    b //= num
    
    while b % 2 == 0:
        b = b // 2
    
    while b % 5 == 0:
        b = b // 5
        
    return 1 if b == 1 else 2