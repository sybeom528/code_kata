# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 12:48:32

def solution(array, height):
    cnt = 0
    for n in sorted(array, reverse = True):
        if n <= height:
            break
        cnt += 1
    
    return cnt