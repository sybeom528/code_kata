# 체육복
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 알고리즘: 그리디
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 16:24:21

def solution(n, lost, reserve):
    answer = 0
    
    have_clothes = [1] * (n+1)
    
    for i in range(1,n + 1):
        if i in lost:
            have_clothes[i] -= 1
        if i in reserve:
            have_clothes[i] += 1
            
    for i in range(1, len(have_clothes)):
        if have_clothes[i] == 0:
            if have_clothes[i-1] == 2:
                have_clothes[i] = 1
                have_clothes[i-1] = 1
            elif (i+1) < len(have_clothes) and have_clothes[i+1] == 2 and have_clothes[i] == 0:
                have_clothes[i] = 1
                have_clothes[i+1] = 1
    
    for n in have_clothes:
        if n > 0:
            answer += 1
    
    return answer - 1