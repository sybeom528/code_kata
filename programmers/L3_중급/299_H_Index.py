# H-Index
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 알고리즘: 정렬
# 작성자: 서윤범
# 작성일: 2026. 07. 16. 15:50:34

def solution(citations):
    
    citations.sort(reverse = True)
    h = 0
    
    for i, c in enumerate(citations):
        if c >= i + 1:
            h += 1
        else:
            break
            
    return h