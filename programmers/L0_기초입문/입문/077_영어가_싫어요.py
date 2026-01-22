# 영어가 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120894
# 알고리즘: 기초
# 작성자: 서윤범
# 작성일: 2026. 01. 22. 12:09:36

def solution(numbers):
    num_dict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,
           'seven':7,'eight':8,'nine':9}
    
    for key, value in num_dict.items():
        numbers = numbers.replace(key, str(value))
    
    return int(numbers)