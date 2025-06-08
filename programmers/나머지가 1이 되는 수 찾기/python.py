def solution(n):
    return [i + 2 for i in range(n) if n % (i + 2) == 1][0]
