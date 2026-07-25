# 오픈채팅방
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 작성자: 서윤범
# 작성일: 2026. 07. 25. 15:58:39

def solution(record):
    answer = []
    
    dic = {}
    
    for i, s in enumerate(record):
        if s[:5] == 'Leave':
            typ, id = s.split()
        else:
            typ, id, nickname = s.split()
        if id not in dic:
            dic[id] = [[[i,typ]], nickname]
        else:
            if typ != 'Change':
                dic[id][0].append([i,typ])
            dic[id][1] = nickname
    
    answer = []
    for key in dic.keys():
        for v in dic[key][0]:
            if v[1] == 'Enter':
                s = str(v[0]) + dic[key][1] + '님이 들어왔습니다.'
            else:
                s = str(v[0]) + dic[key][1] + '님이 나갔습니다.'
            answer.append(s)
    
    
    return [s[1:] for s in sorted(answer)]