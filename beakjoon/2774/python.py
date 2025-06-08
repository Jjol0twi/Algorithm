import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(len(set(sys.stdin.readline().strip())))
