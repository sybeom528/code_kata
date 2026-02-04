# 다항식 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120863
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 04. 20:13:29

def solution(polynomial):
    
    poly = [s.strip() for s in polynomial.split('+')]
    
    x_tot = 0
    b_tot = 0
    for p in poly:
        if 'x' in p:
            if 'x' == p:
                x_tot += 1
            else:
                x_tot += int(p[:-1])
        else:
            b_tot += int(p)
    
    if x_tot == 0:
        return str(b_tot)
    elif b_tot == 0:
        if x_tot == 1:
            return 'x'
        else:
            return str(x_tot) + 'x'
    else:
        if x_tot == 1:
            return 'x + ' + str(b_tot)
        else:
            return str(x_tot) +'x + ' + str(b_tot)