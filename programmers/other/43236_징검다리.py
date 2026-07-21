# 징검다리
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 작성자: 서윤범
# 작성일: 2026. 07. 21. 17:51:12

def solution(distance, rocks, n):
    answer = 0
    
    left = 1
    right = distance
    rocks.sort()
    dist_list = [rocks[0]]
    
    for i in range(1, len(rocks)):
        dist_list.append(rocks[i] - rocks[i-1])
        
    dist_list.append(distance - rocks[-1])
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        temp = 0
        for dist in dist_list:
            if dist + temp < mid:
                cnt += 1
                temp += dist
            else:
                temp = 0
        
        if cnt <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer