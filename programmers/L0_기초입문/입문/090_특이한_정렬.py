# 특이한 정렬
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120880
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 04. 19:44:02

def solution(numlist, n):
    minus = [abs(x - n) for x in numlist]
    minus = sorted(list(set(minus)))
    
    answer = []
    if minus[0] == 0:
        answer.append(n)
        minus = minus[1:]
    for num in minus:
        if num + n in numlist:
            answer.append(num + n)
        if -1 * num + n in numlist:
            answer.append(-1 * num + n)
        
    return answer