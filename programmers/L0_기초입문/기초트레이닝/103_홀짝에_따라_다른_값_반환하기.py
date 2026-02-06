# 홀짝에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 알고리즘: 조건문
# 작성자: 서윤범
# 작성일: 2026. 02. 06. 13:36:54

def solution(n):
    if n % 2 == 0:
        return sum([x**2 for x in range(2,n+1,2)])
    else:
        return sum([x for x in range(1,n+1,2)])