# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:55:32

def solution(my_string, num1, num2):
    
    return ''.join([my_string[:num1],my_string[num2],my_string[num1+1:num2],my_string[num1],my_string[num2+1:]])