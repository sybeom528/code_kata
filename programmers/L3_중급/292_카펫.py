# 카펫
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 알고리즘: 완전탐색, 수학
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 15:13:56

def solution(brown, yellow):
    
    comb = []
    
    for i in range(2, (brown + yellow) // 2):
        if (brown + yellow) % i == 0:
            comb.append([i,(brown + yellow) // i])

    answer = []
    for i,j in comb:
        if (i-2) * (j-2) == yellow:
            answer = [j,i]
            break
    
    return answer