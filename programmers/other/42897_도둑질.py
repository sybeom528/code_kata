# 도둑질
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 작성자: 서윤범
# 작성일: 2026. 07. 20. 19:32:03

def solution(money):
    answer = 0
    n = len(money)
    
    def dynamic(money):
        n = len(money)
        DP = [0 for _ in range(n)]
        DP[0] = money[0]
        DP[1] = max(DP[0], money[1])
        
        for i in range(2, n):
            DP[i] = max(DP[i-2] + money[i], DP[i-1])   
        return DP[n-1]
    
    return max(dynamic(money[1:]), dynamic(money[:-1]))