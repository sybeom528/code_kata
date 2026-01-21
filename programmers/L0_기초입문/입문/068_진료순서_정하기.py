# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:34:58

def solution(emergency):
    
    answer = [0] * len(emergency)
    cnt = 1
    for num in sorted(emergency, reverse = True):
        for i, n in enumerate(emergency):
            if num == n:
                answer[i] = cnt
                cnt += 1
                break
                
    return answer