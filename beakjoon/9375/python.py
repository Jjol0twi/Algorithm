import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    r = 1
    cs = {}
    for i in range(n):
        c, tc = map(str, sys.stdin.readline().split())
        if tc in cs.keys():
            cs[tc]+=1
        else:
            cs[tc] = 1
    for k, v in cs.items():
        r*=(v+1)
        print(k,r)
    print(r-1)
