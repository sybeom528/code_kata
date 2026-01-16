# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 14:46:27

def solution(n):
    answer = 0
    for s in str(n):
        answer += int(s)
    return answer