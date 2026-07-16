# K번째수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 알고리즘: 정렬
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 14:21:37

def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    
    return answer