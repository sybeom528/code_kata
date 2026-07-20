# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 서윤범
# 작성일: 2026. 07. 20. 17:38:44

def solution(triangle):
    answer = 0
    n = len(triangle)
    
    for i in range(n-2, -1, -1):
        for j, num in enumerate(triangle[i]):
            left = num + triangle[i+1][j]
            right = num + triangle[i+1][j+1]
            triangle[i][j] = max(left, right)
    
    return triangle[0][0]