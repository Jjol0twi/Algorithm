def solution(num1, num2):
    """
    if not(0 <= num1 <= 10000 and 0 <= num2 <= 10000):
        exit()
    """
    valid_range = range(0, 10001)
    if not (num1 in valid_range and num2 in valid_range):
        exit()
    """
    if num1 == num2:
        return 1
    else:
        return -1
    """
    return 1 if num1 == num2 else -1
