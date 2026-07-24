# 롤케이크 자르기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 알고리즘: 해시
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 15:04:45

from collections import Counter

def solution(topping):
    answer = 0
    n = len(topping)
    i = 0
    j = n
    mid = (i + j) // 2
    
    left = Counter(topping[:mid])
    right = Counter(topping[mid:])
    
    left_unique = len(left.keys())
    right_unique = len(right.keys())
    
    if left_unique == right_unique:
        answer += 1
        
    def move_left(mid,left,right):
        cnt = 0
        left_unique = len(left.keys())
        right_unique = len(right.keys())
        
        while left_unique >= right_unique:
            mid -= 1
            target = topping[mid]
            left[target] -= 1
            right[target] += 1
            
            if left[target] == 0:
                left_unique -= 1
            if right[target] == 1:
                right_unique += 1
            if left_unique == right_unique:
                cnt += 1
        return cnt
    
    def move_right(mid,left,right):
        cnt = 0
        left_unique = len(left.keys())
        right_unique = len(right.keys())
        
        while left_unique <= right_unique:
            mid += 1
            target = topping[mid-1]
            left[target] += 1
            right[target] -= 1
            if right[target] == 0:
                right_unique -= 1
            if left[target] == 1:
                left_unique += 1
            if left_unique == right_unique:
                cnt += 1
        return cnt
    
    answer += move_left(mid, left.copy(), right.copy())
    answer += move_right(mid, left.copy(), right.copy())
    
    return answer















# from collections import Counter

# def solution(topping):
#     right_dic = dict(Counter(topping))
#     left_dic = dict()
#     right_cnt = len(right_dic)
#     left_cnt = 0
    
#     answer = 0
#     for i in topping:
#         right_dic[i] -= 1
#         if right_dic[i] == 0:
#             right_cnt -= 1
#         if not i in left_dic:
#             left_dic[i] = 1
#             left_cnt += 1
#         if left_cnt == right_cnt:
#             answer += 1
#         if left_cnt > right_cnt:
#             break
    
#     return answer