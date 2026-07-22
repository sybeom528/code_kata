# 연속 부분 수열 합의 개수
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 알고리즘: 해시, 슬라이딩윈도우
# 작성자: 서윤범
# 작성일: 2026. 07. 22. 15:37:51

def solution(elements):
    answer = 0
    
    n = len(elements)
    
    sum_list = [elements[0]]
    
    for i in range(1,n):
        sum_list.append(sum_list[i-1] + elements[i])
    
    for i in range(n):
        sum_list.append(sum_list[i+n-1] + elements[i])
    
    num_list = []
    num_list.extend(sum_list[:n])
    num_list.extend(elements)
    
    for i in range(1,n):
        for j in range(1,n):
            num = sum_list[i+j] - sum_list[i-1]
            num_list.append(num)
    
    return len(list(set(num_list)))