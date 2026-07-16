# 프로세스
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 알고리즘: 스택/큐
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 13:01:40

from collections import defaultdict
import heapq

def solution(priorities, location):
    answer = 0
    dic = defaultdict(list)
    
    for i, p in enumerate(priorities):
        dic[p].append(i)
    
    length = len(priorities)
    now_idx = 0
    chk = False
    for k in sorted(dic, key = lambda x: -x):
        tmp_list = dic[k]
        hq = []
        for tmp in tmp_list:
            if tmp < now_idx:
                heapq.heappush(hq, [length + tmp, tmp])
            else:
                heapq.heappush(hq, [tmp, tmp])
        while hq:
            a, now_idx = heapq.heappop(hq)
            answer += 1
            if now_idx == location:
                chk = True
                break
        if chk:
            break
        
    return answer