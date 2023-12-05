def solution(num1, num2):
    valid_range = range(0, 10001)
    if not (num1 in valid_range and num2 in valid_range):
        exit()
    '''
    if num1 == num2:
        return 1
    else:
        return -1
    '''
    return 1 if num1 == num2 else -1
