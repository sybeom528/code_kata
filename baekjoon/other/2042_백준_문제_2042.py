# 백준 문제 2042
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/2042
# 작성자: 서윤범
# 작성일: 2026. 02. 26. 11:26:52

import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

temp = N
tree_depth = 1

while temp > 1:
    tree_depth += 1
    temp = temp //  2

leaf_start_idx = 2 ** tree_depth

tree = [0 for _ in range(2 ** (tree_depth + 1) + 1)]

for i in range(leaf_start_idx, leaf_start_idx + N):
    tree[i] = int(input())

for i in range(leaf_start_idx - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

def changeVal(idx, value, tree):
    idx = leaf_start_idx + idx - 1
    diff = value - tree[idx]
    tree[idx] = value   
    while idx > 1:
        idx = idx // 2
        tree[idx] += diff    
    return tree

def treeSum(idx1, idx2, tree):
    idx1 = leaf_start_idx + idx1 - 1
    idx2 = leaf_start_idx + idx2 - 1
    result = 0
    while idx1 <= idx2:
        if idx1 % 2 == 1:
            result += tree[idx1]
            idx1 = idx1 + 1
        if idx2 % 2 == 0:
            result += tree[idx2]
            idx2 = idx2 - 1
        idx1 = idx1 // 2
        idx2 = idx2 // 2

    return result
    
for _ in range(M+K):
    q,a,b = map(int, input().split())
    if q == 1:
        tree = changeVal(a,b,tree)
    else:
        print(treeSum(a,b,tree))