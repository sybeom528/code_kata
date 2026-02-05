# 옹알이 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 20:56:47

def solution(babbling):
    can_say = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for word in babbling:
        for say in can_say:
            word = word.replace(say, " ")
            
        if word.strip() == "":
            answer += 1
            
    return answer