import sys
print(len(set([int(sys.stdin.readline())%42 for _ in range(10)])))
