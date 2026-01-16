# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 13:30:20

def solution(my_string, letter):
    answer = ''
    return ''.join(s for s in my_string if s != letter)