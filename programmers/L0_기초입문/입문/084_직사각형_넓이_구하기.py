# 직사각형 넓이 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120860
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 19:20:23

# def solution(dots):
#     min_x = min([d[0] for d in dots])
#     max_x = max([d[0] for d in dots])
#     min_y = min([d[1] for d in dots])
#     max_y = max([d[1] for d in dots])
#     return (max_x - min_x) * (max_y - min_y)

def solution(dots):
    x_coord, y_coord = zip(*dots)
    return (max(x_coord) - min(x_coord)) * (max(y_coord) - min(y_coord))