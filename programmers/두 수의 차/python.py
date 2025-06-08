def solution(num1, num2):
    """
    if not (-50000 <= num1 <= 50000 and -50000 <= num2 <= 50000):
        exit()
    """
    valid_range = range(-50000, 50001)
    if not (num1 in valid_range and num2 in valid_range):
        exit()
    return num1 - num2
