# 로그인 성공?
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 19:13:35

def solution(id_pw, db):
    
    answer = 'fail'
    
    for id, pw in db:
        if id == id_pw[0] and pw == id_pw[1]:
            return 'login'
        elif id == id_pw[0] and pw != id_pw[1]:
            answer = 'wrong pw'
    
    return answer