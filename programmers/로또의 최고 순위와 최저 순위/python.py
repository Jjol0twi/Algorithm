def solution(lottos, win_nums):
    answer = []
    zero=lottos.count(0)
    correct=7
    for a in lottos:
        for b in win_nums:
            if a==b:    correct-=1
    answer.append(correct-zero)
    answer.append(correct)
    for a in answer:
        if a==7:
            answer[answer.index(a)]=6
        if a==0:
            answer[answer.index(a)]=1
    return answer