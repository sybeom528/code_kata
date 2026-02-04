# OX퀴즈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120907
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 04. 21:12:18

def solution(quiz):
    answer = []
    for q in quiz:
        p = q.split()
        
        num1 = int(p[0])
        op = p[1]
        num2 = int(p[2])
        result = int(p[4])
        
        if op == '+':
            tot = num1 + num2
        else:
            tot = num1 - num2
            
        if tot == result:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer