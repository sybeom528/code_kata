# 단어 변환
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 알고리즘: DFS/BFS
# 작성자: 서윤범
# 작성일: 2026. 07. 18. 15:20:09

from collections import deque
import sys

def solution(begin, target, words):    
    
    if target not in words:
        return 0
    else:
        n = len(begin)
        queue = deque()
        queue.append([0, [begin]])
        answer = sys.maxsize
        while queue:
            cnt, word_list = queue.popleft()
            if cnt >= answer:
                continue
            for word in words:
                if word not in word_list:
                    chk = 0
                    chk_word = word_list[-1]
                    for i in range(n):
                        if chk_word[i] != word[i]:
                            chk += 1
                    if chk == 1:
                        if word == target:
                            if cnt + 1 < answer:
                                answer = cnt + 1
                        else:
                            tmp_list = word_list.copy()
                            tmp_list.append(word)
                            queue.append([cnt + 1, tmp_list])
                                    
    if answer == sys.maxsize:
        return 0
    else:
        return answer