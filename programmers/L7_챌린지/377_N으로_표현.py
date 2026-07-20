# N으로 표현
# 프로그래머스 레벨7 (챌린지)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 알고리즘: DP
# 작성자: 서윤범
# 작성일: 2026. 07. 20. 17:26:53

def solution(N, number):
    
    DP = [[] for _ in range(9)]
    
    DP[1] = [N]
    
    if number == DP[1][0]:
        return 1
    
    for i in range(2, 9):
        for j in range(1,i):
            for num1 in DP[j]:
                for num2 in DP[i-j]:
                    temp = [num1 + num2, num1 - num2, num1 * num2]
                    if num2 != 0:
                        temp.append(num1 // num2)
                    DP[i].extend(temp)
        DP[i] = list(set(DP[i]))
        DP[i].append(int(str(N) * i))
        if number in DP[i]:
            return i

    return -1