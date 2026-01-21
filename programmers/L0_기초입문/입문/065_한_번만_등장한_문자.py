# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 10:06:32

from collections import Counter

def solution(s):
    answer = ''
    
    s_dict = Counter(s)
    
    for k,v in s_dict.items():
        if v == 1:
            answer += k
            
    return ''.join(sorted(answer))