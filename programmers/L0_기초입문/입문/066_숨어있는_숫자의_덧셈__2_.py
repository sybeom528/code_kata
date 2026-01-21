# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:16:15

def solution(my_string):
    
    num_list = []
    chk = False
    my_string = my_string + 'a'
    
    for s in my_string:
        if s.isalpha() and not chk:
            continue
        elif s.isalpha() and chk:
            chk = False
            num_list.append(int(tmp))
        elif s.isdigit() and not chk:
            tmp = s
            chk = True
        elif s.isdigit() and chk:
            tmp += s

    return sum(num_list)