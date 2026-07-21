# 입국심사
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 알고리즘: 이진탐색
# 작성자: 서윤범
# 작성일: 2026. 07. 21. 16:42:40

def solution(n, times):

    i = 0
    j = max(times) * n
    
    while i < j:
        cnt = 0
        mid = (i + j) // 2
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            j = mid
            
        elif cnt < n:
            i = mid + 1
            
    return i