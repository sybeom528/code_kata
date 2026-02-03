# 치킨 쿠폰
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 19:53:05

def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        chicken = coupon // 10
        coupon = coupon % 10 + chicken
        answer += chicken
    
    return answer