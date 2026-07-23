# 전화번호 목록
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 15:07:38

def solution(phone_book):
    
    phone_book.sort()
    n = len(phone_book)
    
    for i in range(n - 1):
        m = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:m]:
            return False
    
    return True













# def solution(phone_book):
#     answer = True
    
#     phone_book.sort()
    
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#             answer = False
#             break
    
#     return answer