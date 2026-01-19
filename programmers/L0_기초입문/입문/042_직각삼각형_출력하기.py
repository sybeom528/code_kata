# 직각삼각형 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120823
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:33:22

n = int(input())

for i in range(n):
    print('*' * (i + 1), ' ' * (n - i - 1))