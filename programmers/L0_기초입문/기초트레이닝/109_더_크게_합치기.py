# 더 크게 합치기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181939
# 알고리즘: 연산
# 작성자: 서윤범
# 작성일: 2026. 02. 06. 13:47:52

def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    return max(num1, num2)