# 잘라서 배열로 저장하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 10:13:37

def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]