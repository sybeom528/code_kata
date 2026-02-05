# 안전지대
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 05. 10:33:49

def solution(board):
    
    check = [[0 for _ in range(len(board))] for _ in range(len(board))]
    
    n = len(board)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        now_x, now_y = i + dx, j + dy
                        if 0 <= now_x < n and 0 <= now_y < n and check[now_x][now_y] == 0:
                            check[now_x][now_y] = 1
    
    
    tot = sum([sum(l) for l in check])
    
    answer = len(board) ** 2 - tot
    return answer