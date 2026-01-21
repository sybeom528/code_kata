# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 21. 09:58:47

from collections import Counter

def solution(before, after):
    
    answer = 1
    
    prev_dict = Counter(before)
    after_dict = Counter(after)
    
    for k, v in prev_dict.items():
        if k in after_dict and v == after_dict[k]:
            continue
        else:
            answer = 0
            break
    
    return answer