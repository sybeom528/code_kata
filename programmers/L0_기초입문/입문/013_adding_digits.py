def solution(n):
    return sum([int(s) for s in str(n)])

if __name__ == '__main__':
    print(solution(123))
    print(solution(987))