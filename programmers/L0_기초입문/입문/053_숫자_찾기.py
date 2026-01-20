# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 20. 10:00:57

def solution(num, k):
    answer = -1
    for i, s in enumerate(str(num)):
        if k == int(s):
            answer = i + 1
            break
    return answer