# 백준 문제 1929
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1929
# 작성자: 서윤범
# 작성일: 2026. 02. 20. 11:43:58

import sys
import math

M,N = map(int, input().split())

A = [1 for _ in range(N + 1)]
A[0] = 0
A[1] = 0

for i in range(2, int(math.sqrt(N)) + 1):
    if A[i] == 0:
        continue
    for j in range(i * 2,N + 1,i):
        A[j] = 0

for i in range(M,N + 1):
    if A[i] == 1:
        print(i)