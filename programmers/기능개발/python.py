def solution(progresses, speeds):
    _progresses = [(100 - i) // j + ((100-i) % j > 0) for i, j in zip(progresses, speeds)]
    answer = []
    while _progresses:
        count = 0
        while _progresses[count:] and _progresses[count] <= _progresses[0]:
            count+=1
        del _progresses[:count]
        answer.append(count)
    return answer
