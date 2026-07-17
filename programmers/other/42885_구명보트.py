# 구명보트
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 16:55:11

def solution(people, limit):
    
    check = [True] * len(people)
    people.sort()
    answer = 0
    
    i = 0
    j = len(people) - 1
    
    while i < j:
        while j > 0 and people[i] + people[j] > limit:
            j -= 1
        check[i] = False
        check[j] = False
        answer += 1
        i += 1
        j -= 1
    
    return answer + sum(check)