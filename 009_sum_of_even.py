def solution(n):
    return 0 if n < 2 else sum([i for i in range(2,n + 1,2)])

if __name__ == '__main__':
    print(solution(10))
    print(solution(4))