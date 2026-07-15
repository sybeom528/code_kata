# 의상
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 알고리즘: 해시, 수학
# 작성자: 서윤범
# 작성일: 2026. 07. 15. 20:08:46

def solution(clothes):
    
    clo_dict = {}
    
    for clo, typ in clothes:
        if typ not in clo_dict:
            clo_dict[typ] = [clo]
        else:
            clo_dict[typ].append(clo)
    
    length = []
    for key in clo_dict.keys():
        length.append(len(clo_dict[key]) + 1)
        
    answer = 1
    for num in length:
        answer *= num
    
    return answer - 1