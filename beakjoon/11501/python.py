import sys
t = int(sys.stdin.readline())
for _ in range(t):
    r = 0
    d = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()[:d]))
    max = 0
    for i in range(d-1,-1,-1):
        if l[i]>max:
            max=l[i]
        else:
            r+=max-l[i]
    print(r)
