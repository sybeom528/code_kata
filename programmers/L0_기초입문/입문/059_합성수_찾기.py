# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:28:36

def solution(n):
    num_list = [0] * (n + 1)
    for i in range(2,n + 1):
        if num_list[i] == 1:
            continue
        else:
            for j in range(i * 2, n + 1, i):
                num_list[j] = 1
    
    return sum(num_list)