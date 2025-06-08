def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]
    steps = [[1, 0], [0, 1], [-1, -1]]
    num = 1
    cur_coords = [-1, 0]
    for i in reversed(range(n + 1)):
        step = steps[(n - i) % len(steps)]
        for j in range(i):
            cur_coords = [a + b for a, b in zip(cur_coords, step)]
            answer[cur_coords[0]][cur_coords[1]] = num
            num += 1
    return [j for i in answer for j in i]
    # return sum(answer,[]) 이 방법은 신기하지만 시간이 더 걸린다.
