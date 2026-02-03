# 저주의 숫자 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 20:22:54

def solution(n):
    answer = 0
    
    while n > 0:
        answer += 1
        while (answer % 3) == 0 or '3' in str(answer):
            answer += 1
        n -= 1
        
    return answer