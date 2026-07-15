# 베스트앨범
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 알고리즘: 해시, 정렬
# 작성자: 서윤범
# 작성일: 2026. 07. 15. 20:43:03

def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [plays[i], [[plays[i], i]]]
        else:
            genre_dict[genres[i]][0] += plays[i]
            genre_dict[genres[i]][1].append([plays[i],i])
            genre_dict[genres[i]][1].sort(key = lambda x: (-x[0], x[1]))
    
    genre_sorted = sorted(genre_dict.items(), key = lambda x: (-x[1][0]))
    
    for i in range(len(genre_sorted)):
        for j in range(min(2, len(genre_sorted[i][1][1]))):
            answer.append(genre_sorted[i][1][1][j][1])
    
    return answer