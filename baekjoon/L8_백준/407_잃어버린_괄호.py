# 잃어버린 괄호
# 백준 레벨8 (백준)
# 문제 링크: https://www.acmicpc.net/problem/1541
# 알고리즘: 그리디
# 작성자: 서윤범
# 작성일: 2026. 02. 20. 11:33:35

import sys
sys.setrecursionlimit(10**6)

num_list = input().split('-')
answer = 0

for i, l in enumerate(num_list):
    plus = l.split('+')
    tmp = 0
    for p in plus:
        tmp += int(p)
    if i == 0:
        answer += tmp
    else:
        answer -= tmp

print(answer)