# flag에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181933
# 알고리즘: 조건문
# 작성자: 서윤범
# 작성일: 2026. 02. 06. 13:38:41

def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b
    