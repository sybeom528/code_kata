# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 20:49:21

from math import floor

def solution(price):
    return price if price < 100000 else floor(price * 0.95) if price < 300000 else floor(price * 0.9) if price < 500000 else floor(price * 0.8)

