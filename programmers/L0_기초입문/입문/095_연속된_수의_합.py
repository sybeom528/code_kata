# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 09:47:40

def solution(num, total):
    mid = total / num
    if mid == int(mid):
        answer = [mid]
        for i in range(1,(num // 2) + 1):
            answer.append(mid+i)
            answer.append(mid-i)
    else:
        mid1, mid2 = int(mid-0.5), int(mid+0.5)
        answer = [mid1, mid2]
        for i in range(1, (num - 2) // 2 + 1):
            answer.append(mid1-i)
            answer.append(mid2+i)
    
    return sorted(answer)