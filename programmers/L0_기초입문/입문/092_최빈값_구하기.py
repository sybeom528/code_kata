# 최빈값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 04. 20:25:55

from collections import Counter

def solution(array):
    
    dic = Counter(array)
    
    items = sorted(dic.items(), key = lambda x: -x[1])
    
    if len(items) == 1:
        return items[0][0]
    elif items[0][1] == items[1][1]:
        return -1
    else:
        return items[0][0]