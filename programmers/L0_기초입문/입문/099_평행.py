# 평행
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 20:43:54

def solution(dots):
    
    idx = [[0,1,2,3],[0,2,1,3],[0,3,1,2]]
    
    dots.sort(key = lambda x: (x[0],x[1]))
    
    for i,j,k,l in idx:
        grad1 = (dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0])
        grad2 = (dots[l][1] - dots[k][1]) / (dots[l][0] - dots[k][0])
        if grad1 == grad2:
            return 1
    
    return 0