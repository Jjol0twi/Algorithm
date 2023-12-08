def solution(a, b):
    return sum(i for i in range(a,b+(1 if a<=b else -1),1 if a<=b else -1))