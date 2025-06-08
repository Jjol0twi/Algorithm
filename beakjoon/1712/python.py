import sys
a, b, c = map(int, sys.stdin.readline().split())
if b < c:
    d = a//c    # result
    e = a%c + d*b   # 남은 돈
    d += e//(c-b)
    e %= (c-b)
    if e<0:
        print(d)
    else:
        print(d+1)
else:
    print(-1)
