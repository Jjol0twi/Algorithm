def solution(arr):
    answer=[arr[0] if arr else []]
    for i in arr[1:]:
        if i!=answer[-1]:
            answer.append(i)
    return answer
