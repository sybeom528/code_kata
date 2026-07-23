# 가장 큰 수
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 알고리즘: 정렬
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 17:19:41

from functools import cmp_to_key

def solution(numbers):
    
    def sort_numbers(a,b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
        
    str_numbers = [str(num) for num in numbers]
    str_numbers.sort(key = cmp_to_key(sort_numbers))
    
    if str_numbers[0] == '0':
        return '0'
    else:
        return ''.join(str_numbers)













# from functools import cmp_to_key

# def cmp(a, b):
#     if a + b > b + a: return -1
#     elif a + b < b + a: return 1
#     else: return 0

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=cmp_to_key(cmp))
#     if numbers[0] == '0':
#         return '0'
#     else:
#         return ''.join(numbers)
