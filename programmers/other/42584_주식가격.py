# 주식가격
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 14:14:38

def solution(prices):
    
    stack = []
    answer = [0] * len(prices)
    
    for i, p in enumerate(prices):
        if not stack:
            stack.append([p,i])
        else:
            while stack and stack[-1][0] > p:
                _, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([p,i])
            
    while stack:
        _,i = stack.pop()
        answer[i] = len(prices) - i - 1
    
    return answer