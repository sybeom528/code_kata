# 거리두기 확인하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 알고리즘: BFS, 시뮬레이션
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 13:50:35

from collections import deque

def BFS(place):
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                queue = deque()
                queue.append((i,j,0))
                
                while queue:
                    x,y,cnt = queue.popleft()
                    if cnt == 2:
                        continue
                    chk = False
                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < 5 and 0 <= next_y < 5 and not (next_x == i and next_y == j) and place[x][y] != 'X':
                            if place[next_x][next_y] == 'P':
                                return 0

                            else:
                                queue.append((next_x, next_y, cnt + 1))

    return 1
                

def solution(places):
    answer = []
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    chk = True
    
    for place in places:
        chk = BFS(place)
        answer.append(chk)
                    
    return answer