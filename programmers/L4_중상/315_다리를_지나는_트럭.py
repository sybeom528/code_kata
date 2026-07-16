# 다리를 지나는 트럭
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 알고리즘: 스택/큐, 시뮬레이션
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 13:47:13

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    now_weights = 0
    answer = 0
    
    while bridge:
        answer += 1
        now_weights -= bridge.popleft()
        
        if truck_weights:
            if now_weights + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                now_weights += t
            else:
                bridge.append(0)
    
    return answer