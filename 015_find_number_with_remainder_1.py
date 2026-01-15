def solution(n):
    for i in range(2,n):
        if n % i == 1:
            answer = i
            break
    
    return answer

if __name__ == '__main__':
    print(solution(10))
    print(solution(12))