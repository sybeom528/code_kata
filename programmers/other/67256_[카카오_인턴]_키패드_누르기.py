# [카카오 인턴] 키패드 누르기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 작성자: 서윤범
# 작성일: 2026. 07. 15. 19:38:19

def solution(numbers, hand):
    answer = ''
    left_xy = [3,0]
    right_xy = [3,2]
    
    for i,s in enumerate(numbers):
        if s in [1,4,7]:
            answer += 'L'
            left_xy = [0,0] if s == 1 else [1,0] if s == 4 else [2,0]
        elif s in [3,6,9]:
            answer += 'R'
            right_xy = [0,2] if s == 3 else [1,2] if s == 6 else [2,2]
        else:
            now_xy = [0,1] if s == 2 else [1,1] if s == 5 else [2,1] if s == 8 else [3,1]
            if (abs(now_xy[0] - left_xy[0]) + abs(now_xy[1] - left_xy[1])) < (abs(now_xy[0] - right_xy[0]) + abs(now_xy[1] - right_xy[1])):
                
                answer += 'L'
                left_xy = now_xy
            elif (abs(now_xy[0] - left_xy[0]) + abs(now_xy[1] - left_xy[1])) > (abs(now_xy[0] - right_xy[0]) + abs(now_xy[1] - right_xy[1])):
                answer += 'R'
                right_xy = now_xy
            else:
                if hand == 'left':
                    answer += 'L'
                    left_xy = now_xy
                else:
                    answer += 'R'
                    right_xy = now_xy
            
    
    return answer