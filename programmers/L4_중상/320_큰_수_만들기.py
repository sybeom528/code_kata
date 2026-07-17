# 큰 수 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 알고리즘: 그리디, 스택
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 16:46:09

def solution(number, k):
    
    remove_cnt = 0
    answer = ''
    idx = 0
    stack = []
    
    while idx < len(number):
        while stack and (remove_cnt < k) and (stack[-1] < int(number[idx])):
            stack.pop()
            remove_cnt += 1
        stack.append(int(number[idx]))
        idx += 1
        
    if remove_cnt < k:
        while remove_cnt < k:
            stack.pop()
            remove_cnt += 1
        
    for s in stack:
        answer += str(s)
        
    return answer