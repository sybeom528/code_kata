# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 19. 10:49:50

def solution(cipher, code):
    return ''.join(s for i, s in enumerate(cipher) if (i + 1) % code == 0)