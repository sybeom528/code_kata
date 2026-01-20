# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:18:05

from collections import deque

def solution(numbers, direction):
    answer = deque(numbers)
    if direction == 'right':
        num = answer.pop()
        answer.appendleft(num)
    else:
        num = answer.popleft()
        answer.append(num)
    return list(answer)