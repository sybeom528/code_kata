# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:42:18

def solution(array, n):
    
    array = sorted(array)
    
    if n <= array[0]:
        return array[0]
    elif n >= array[-1]:
        return array[-1]
    else:    
        for i in range(len(array) - 1):
            if array[i] == n:
                return array[i]
            elif array[i] < n and array[i + 1] > n:
                if abs(array[i] - n) <= abs(array[i + 1] - n):
                    return array[i]
                else:
                    return array[i + 1]