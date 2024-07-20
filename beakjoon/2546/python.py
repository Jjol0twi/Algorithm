import sys

t = int(sys.stdin.readline())
for _ in range(t):
    sys.stdin.readline()
    r = 0
    n, m = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()[:n]))
    e = list(map(int, sys.stdin.readline().split()[:m]))
    ca = sum(c) / n
    ea = sum(e) / m
    sc = sum(c)
    se = sum(e)
    for i in range(n):
        if ca > c[i] > ea:
            nc = (sc - c[i]) / (n - 1)
            ne = (se + c[i]) / (m + 1)
            if ca < nc and ea < ne:
                r += 1
    print(r)
