# 외계어 사전
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120869
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 02. 03. 18:01:55

def solution(spell, dic):
    spell_set = set(spell)
    for d in dic:
        if len(d) == len(spell) and set(d) == spell_set:
            return 1
    return 2