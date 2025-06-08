def solution(sequence, k):
    start, end, current_sum = 0, 0, 0
    min_length = float('inf')
    result = []
    while end < len(sequence):
        current_sum += sequence[end]
        while current_sum >= k:
            if end - start < min_length:
                min_length = end - start
                result = [start, end]
            current_sum -= sequence[start]
            start += 1
        end += 1
    return result
