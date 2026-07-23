# 신규 아이디 추천
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/72410
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 15:03:31

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    tmp_id = ''
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in ['-','_','.']:
            tmp_id += s
            
    while '..' in tmp_id:
        tmp_id = tmp_id.replace('..','.')
        
    if len(tmp_id) > 0 and tmp_id[0] == '.':
        tmp_id = tmp_id[1:]
    if len(tmp_id) > 0 and tmp_id[-1] == '.':
        tmp_id = tmp_id[:-1]
        
    if tmp_id == '':
        tmp_id = 'a'
    
    if len(tmp_id) >= 16:
        tmp_id = tmp_id[:15]
    if tmp_id[-1] == '.':
        tmp_id = tmp_id[:-1]
        
    if len(tmp_id) <= 2:
        while len(tmp_id) < 3:
            tmp_id += tmp_id[-1]
    
    return tmp_id












# def solution(new_id):
#     # 1. 소문자 치환
#     new_id = new_id.lower()
    
#     # 2. 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
#     tmp_id = ''
#     include_str = ['-','_','.']
#     for s in new_id:
#         if s.isdigit() or s.isalpha() or s in include_str:
#             tmp_id += s
    
#     # 3. 마침표 2번이상 -> 하나의 마침표
    
#     while '..' in tmp_id:
#         tmp_id = tmp_id.replace('..','.')
    
#     # 4. 마침표 처음 끝 제거
#     if tmp_id[0] == '.':
#         tmp_id = tmp_id[1:]
#     elif tmp_id[-1] == '.':
#         tmp_id = tmp_id[:-1]
        
#     # 5. 빈 문자열일 시 'a' 대입
#     if tmp_id == '':
#         tmp_id = 'a'
        
#     # 6. new_id 16자 이상이면 첫 15자 제외
#     if len(tmp_id) >= 16:
#         tmp_id = tmp_id[:15]
#     if tmp_id[-1] == '.':
#         tmp_id = tmp_id[:-1]
    
#     # 7. tmp_id 2자 이하면 마지막 문자 반복
#     if len(tmp_id) <= 2:
#         while len(tmp_id) < 3:
#             tmp_id += tmp_id[-1]
            
#     answer = tmp_id
#     return answer