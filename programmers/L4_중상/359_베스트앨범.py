# 베스트앨범
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 알고리즘: 해시, 정렬
# 작성자: 서윤범
# 작성일: 2026. 07. 23. 15:31:22

def solution(genres, plays):
    answer = []
    
    dic = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = [play, [[idx, play]]]
        else:
            dic[genre][0] += play
            dic[genre][1].append([idx, play])
    
    for key in dic.keys():
        dic[key][1].sort(key = lambda x: (-x[1], x[0]))
                
    sort_dic = sorted(dic.items(), key = lambda x: - x[1][0] )
    
    for _, lst in sort_dic:
        for i in range(min(2, len(lst[1]))):
            answer.append(lst[1][i][0])
    
    return answer




















# AI 풀이
# 애초에 두 개의 다른 딕셔너리를 만들어서 sorted하는 구조
# from collections import defaultdict

# def solution(genres, plays):
#     total = defaultdict(int)
#     songs = defaultdict(list)
#     answer = []
    
#     for i, (g,p) in enumerate(zip(genres, plays)):
#         total[g] += p
#         songs[g].append([p,i])
        
#     for g in sorted(total, key = lambda x: -total[x]):
#         top = sorted(songs[g], key = lambda x: (-x[0], x[1]))
#         answer += [i for p, i in top[:2]]
    
#     return answer



# 내 풀이
# def solution(genres, plays):
#     answer = []
    
#     genre_dict = {}
    
#     for i in range(len(genres)):
#         if genres[i] not in genre_dict:
#             genre_dict[genres[i]] = [plays[i], [[plays[i], i]]]
#         else:
#             genre_dict[genres[i]][0] += plays[i]
#             genre_dict[genres[i]][1].append([plays[i],i])
#             genre_dict[genres[i]][1].sort(key = lambda x: (-x[0], x[1]))
    
#     genre_sorted = sorted(genre_dict.items(), key = lambda x: (-x[1][0]))
    
#     for i in range(len(genre_sorted)):
#         for j in range(min(2, len(genre_sorted[i][1][1]))):
#             answer.append(genre_sorted[i][1][1][j][1])
    
#     return answer