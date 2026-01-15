from math import floor

def solution(num1, num2):
    return floor(num1 / num2 * 1000)

if __name__ == '__main__':
    print(solution(3,2))
    print(solution(7,3))
    print(solution(1,16))