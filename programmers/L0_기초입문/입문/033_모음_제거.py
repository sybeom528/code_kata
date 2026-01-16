# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 13:31:18

def solution(my_string):
    return ''.join(s for s in my_string if s not in 'aeiou')