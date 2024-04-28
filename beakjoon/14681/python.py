import sys
x, y = [int(sys.stdin.readline().strip()) for _ in range(2)]
match (x > 0, y > 0):
    case (True, True):
        print(1)
    case (False, True):
        print(2)
    case (False, False):
        print(3)
    case (True, False):
        print(4)
