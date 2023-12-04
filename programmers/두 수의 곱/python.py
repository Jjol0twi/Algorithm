def solution(num1, num2):
    answer = 0
    '''
    if not (0 <= num1 <= 100 and 0 <= num2 <= 100):
        exit()
    '''
    valid_range = range(0, 101)
    if not(num1 in valid_range and num2 in valid_range):
        exit()
    return num1 * num2