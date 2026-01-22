# 캐릭터의 좌표
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120861
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 12:26:11

def solution(keyinput, board):
    
    max_x = (board[0] - 1) // 2
    max_y = (board[1] - 1) // 2
    
    move = {'left':[-1,0], 'right':[1,0], 'up':[0,1], 'down':[0,-1]}
    
    now_x, now_y = 0, 0
    
    for m in keyinput:
        dx, dy = move[m]
        if abs(now_x + dx) <= max_x and abs(now_y + dy) <= max_y:
            now_x += dx 
            now_y += dy
            
    return [now_x, now_y]