# 개인정보 수집 유효기간
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 알고리즘: 시뮬레이션, 문자열
# 작성자: 서윤범
# 작성일: 2026. 07. 24. 14:31:19

def solution(today, terms, privacies):
    answer = []
    
    term_dic = {}
    for term in terms:
        typ, mon = term.split()
        term_dic[typ] = int(mon)
    
    now_y, now_m, now_d = today.split('.')
    now_y = int(now_y); now_m = int(now_m); now_d = int(now_d)
    
    for i, p in enumerate(privacies):
        chk = False
        date, typ = p.split()
        year, month, day = date.split('.')
        year = int(year); month = int(month); day = int(day)
        duration = term_dic[typ]
        dy = duration // 12
        dm = duration % 12
        if month + dm > 12:
            month = month + dm - 12
            dy += 1
        else:
            month += dm
        year += dy
        if day - 1 == 0:
            day = 28
            month -= 1
        else:
            day -= 1
        
        if now_y > year:
            chk = True
        elif now_y == year:
            if now_m > month:
                chk = True
            elif now_m == month:
                if now_d > day:
                    chk = True
                    
        if chk:
            answer.append(i + 1)
        
    return answer
















# def solution(today, terms, privacies):
    
#     year, month ,day = map(int, today.split('.'))
#     date_num = year * 10000 + month * 100 + day
    
#     term = {}
#     for i in range(len(terms)):
#         a,b = terms[i].split(' ')
#         term[a] = int(b)
    
#     answer = []
#     for i in range(len(privacies)):
#         date, c = privacies[i].split(' ')
#         y,m,d = map(int, date.split('.'))
#         d -= 1
#         if d < 1:
#             d = 28
#             m -= 1
#             if m < 0:
#                 m = 12
#         m += term[c]
#         while m > 12:
#             y += 1
#             m -= 12
#         tmp_num = y * 10000 + m * 100 + d
#         if date_num > tmp_num:
#             answer.append(i+1)
    
#     return answer