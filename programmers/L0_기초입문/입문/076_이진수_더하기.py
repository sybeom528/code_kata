# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 12:04:46

def solution(bin1, bin2):
    
    answer = []
    
    bin1 = '0' * (max(len(bin1), len(bin2)) - len(bin1)) + bin1
    bin2 = '0' * (max(len(bin1), len(bin2)) - len(bin2)) + bin2
    
    tmp = 0
    for i in range(len(bin1) - 1, -1, -1):
        now = int(bin1[i]) + int(bin2[i]) + tmp
        if now > 1:
            answer.append(now - 2)
            tmp = 1
        else:
            answer.append(now)
            tmp = 0
    
    if tmp == 1:
        answer.append(1)
        
    ans = ''
    for i in range(len(answer)-1,-1,-1):
        ans += str(answer[i])
    
    return ans