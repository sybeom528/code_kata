# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:37:04

def solution(hp):
    answer = 0
    chk_zero = False
    for num in [5,3,1]:
        if hp % 5 == 0:
            answer += (hp // num)
            chk_zero = True
            break
        else:
            answer += (hp // num)
            hp = hp % num
        
        if chk_zero:
            break
    
    return answer