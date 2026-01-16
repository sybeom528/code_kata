# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 16. 17:52:34

# def solution(array):
#     array = sorted(array)
#     return array[len(array) // 2]

import statistics

def solution(array):
    return statistics.median(array)