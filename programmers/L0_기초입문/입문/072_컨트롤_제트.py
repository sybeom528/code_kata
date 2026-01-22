# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 10:44:21

def solution(s):
    
    answer = []
    
    for c in s.split():
        if c == 'Z':
            answer.pop()
        else:
            answer.append(int(c))
    
    return sum(answer)