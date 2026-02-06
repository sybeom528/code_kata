# 홀짝 구분하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181944
# 알고리즘: 출력
# 작성자: 서윤범
# 작성일: 2026. 02. 06. 13:31:06

a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')