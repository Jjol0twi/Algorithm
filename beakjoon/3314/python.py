import sys
r, c = map(int, sys.stdin.readline().split())
for i in range(r):
    tc = list(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().split()[:c]))
    print(r,c,tc)
