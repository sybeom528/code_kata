# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 13:07:56

def solution(n):
    return sum([1 if n % i == 0 else 0 for i in range(1,n + 1)])