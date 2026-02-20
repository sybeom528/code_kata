# 백준 문제 1920
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1920
# 작성자: 서윤범
# 작성일: 2026. 02. 20. 11:23:12

import sys
sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())

A = list(map(int, input().split()))
A.sort()

M = int(input())

B = []
B = list(map(int, input().split()))

def binary_search(num_list,num):
    i,j = 0, len(num_list) - 1
    while i <= j:
        mid = (i + j) // 2
        if num == num_list[mid]:
            return 1
        elif num > num_list[mid]:
            i = mid + 1
        elif num < num_list[mid]:
            j = mid - 1
    return 0

for num in B:
    print(binary_search(A, num))