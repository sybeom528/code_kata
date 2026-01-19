# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:40:10

def solution(rsp):
    return ''.join(['0' if s == '2' else '5' if s == '0' else '2' for s in rsp])