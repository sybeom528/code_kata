def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3   
    else:
        return 4
    
if __name__ == '__main__':
    print(solution(70))
    print(solution(91))
    print(solution(180))