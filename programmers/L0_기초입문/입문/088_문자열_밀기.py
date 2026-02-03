# 문자열 밀기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120921
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 20:31:07

def solution(A, B):
    if A == B:
        return 0
    
    s = B
    cnt = 0
    for i in range(len(B)):
        s = s[1:] + s[0]
        cnt += 1
        if s == A:
            return cnt
    
    return -1