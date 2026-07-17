# 조이스틱
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 알고리즘: 그리디
# 작성자: 서윤범
# 작성일: 2026. 07. 17. 18:17:24

def solution(name):
    answer = 0
    n = len(name)
    
    # 알파벳 이동
    for i in range(n):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
    
    # 위치 이동
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        min_move = min(
            min_move,
            (i * 2) + n - next_idx,
            (n - next_idx) * 2 + i
        )
    answer += min_move
    
    return answer