# 등수 매기기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120882
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 20:02:50

def solution(score):
    avg = [sum(x) / len(x) for x in score]
    sorted_answer = sorted(avg, reverse = True)
    
    answer = [sorted_answer.index(x) + 1 for x in avg]
    
    return answer