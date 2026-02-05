# 다음에 올 숫자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120924
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 09:23:37

def solution(common):
    
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] // common[0])