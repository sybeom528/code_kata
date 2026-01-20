# 2차원으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 20:47:07

def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        tmp = []
        for j in range(i, i + n):
            tmp.append(num_list[j])
        answer.append(tmp)
        
    return answer