# 공 던지기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 11:18:26

def solution(numbers, k):
    
    return numbers[(((k - 1) * 2) % len(numbers))]