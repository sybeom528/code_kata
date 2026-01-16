# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 14:44:04

def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    
    return answer