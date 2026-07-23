# 단어 변환
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 알고리즘: DFS/BFS
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 18:03:18

from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    n = len(words)
    
    answer = 0
    visited = [False] * n
    
    queue = deque()
    queue.append((0,begin))
    
    while queue:
        cnt, word = queue.popleft()
        if word == target:
            return cnt
        for i in range(n):
            if not visited[i]:
                chk = 0
                for s1, s2 in zip(word, words[i]):
                    if s1 != s2:
                        chk += 1
                if chk == 1:
                    queue.append((cnt + 1, words[i]))
                    visited[i] = True
    
    return answer

















# from collections import deque

# def solution(begin, target, words):
#     if target not in words:
#         return 0
    
#     n = len(begin)
#     visited = {begin}
#     queue = deque()
#     queue.append((begin, 0))
    
#     while queue:
#         word, cnt = queue.popleft()
        
#         if word == target:
#             return cnt
        
#         for next_word in words:
#             if next_word in visited:
#                 continue
#             diff = sum(1 for a, b in zip(word, next_word) if a != b)
#             if diff == 1:
#                 visited.add(next_word)
#                 queue.append((next_word, cnt + 1))
                
#     return 0



# from collections import deque
# import sys

# def solution(begin, target, words):    
    
#     if target not in words:
#         return 0
#     else:
#         n = len(begin)
#         queue = deque()
#         queue.append([0, [begin]])
#         answer = sys.maxsize
#         while queue:
#             cnt, word_list = queue.popleft()
#             if cnt >= answer:
#                 continue
#             for word in words:
#                 if word not in word_list:
#                     chk = 0
#                     chk_word = word_list[-1]
#                     for i in range(n):
#                         if chk_word[i] != word[i]:
#                             chk += 1
#                     if chk == 1:
#                         if word == target:
#                             if cnt + 1 < answer:
#                                 answer = cnt + 1
#                         else:
#                             tmp_list = word_list.copy()
#                             tmp_list.append(word)
#                             queue.append([cnt + 1, tmp_list])
                                    
#     if answer == sys.maxsize:
#         return 0
#     else:
#         return answer

