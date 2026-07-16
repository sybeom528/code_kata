# 기능개발
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 알고리즘: 스택/큐
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 12:22:45

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    days = deque()
    
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        days.append(day)
        
    while days:
        d = days.popleft()
        cnt = 1
        while days and d >= days[0]:
            cnt += 1
            days.popleft()
        answer.append(cnt)
            
    
    return answer