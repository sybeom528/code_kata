# 모의고사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 알고리즘: 완전탐색
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 14:24:43

def solution(answers):
    
    std1 = [1,2,3,4,5]
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]
    
    len1 = len(std1)
    len2 = len(std2)
    len3 = len(std3)
    
    ans_list = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == std1[i % len1]:
            ans_list[0] += 1
        if ans == std2[i % len2]:
            ans_list[1] += 1
        if ans == std3[i % len3]:
            ans_list[2] += 1
    
    max_ans = max(ans_list)
    answer = []
    for i in range(3):
        if ans_list[i] == max_ans:
            answer.append(i + 1)
    
    return answer