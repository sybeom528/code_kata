def solution(n):
    return 0 if n == 0 else sum([i for i in range(1,n + 1) if n % i == 0])

if __name__ == '__main__':
    print(solution(12))
    print(solution(5))