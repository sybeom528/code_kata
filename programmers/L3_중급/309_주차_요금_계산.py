# 주차 요금 계산
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 알고리즘: 해시, 시뮬레이션
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 13:18:58

# fees : [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]

from collections import deque
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    
    dic = defaultdict(list)
    
    for record in records:
        time, num, inout = record.split()
        hour, minute = time.split(':')
        time = int(hour) * 60 + int(minute)
        
        if inout == 'IN':
            dic[num].append([time,-1])
        else:
            dic[num][-1][1] = time
        
    print(dic)
    for key in sorted(dic.keys()):
        cum_time = 0
        for a,b in dic[key]:
            if b == -1:
                b = 1439
            cum_time += b - a
        
        if cum_time <= fees[0]:
            fee = fees[1]
            
        else:
            fee = fees[1] + math.ceil((cum_time - fees[0]) / fees[2]) * fees[3]
        
        answer.append(fee)
    
    return answer