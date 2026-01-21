# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:19:53

def solution(array):
    return sum([str(num).count('7') for num in array])