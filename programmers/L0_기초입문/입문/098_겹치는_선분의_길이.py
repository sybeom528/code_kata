# 겹치는 선분의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 20:23:41

def solution(lines):
    
    counts = {}

    for start, end in lines:
        for i in range(start, end):
            counts[i] = counts.get(i, 0) + 1

    answer = 0
    for val in counts.values():
        if val >= 2:
            answer += 1
            
    return answer