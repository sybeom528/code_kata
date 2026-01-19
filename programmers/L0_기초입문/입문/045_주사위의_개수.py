# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:43:19

def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)