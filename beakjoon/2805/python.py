from sys import stdin

def gb(a, b):
    c = a
    a = (a + b) // 2
    return a, c

n, m = map(int, stdin.readline().split())
tl = sorted(list(map(int, stdin.readline().split()[:n])), reverse=True)
r, _r = (sum(tl) - m) // n, 0
while True:
    x = 0
    for i in range(n):
        x += max(0, tl[i] - r)  # x += tl[i] - r if tl[i] - r > 0 else 0
        if x>m:
            _r = tl[i]
            break
    if x != m:
        print(r,_r)
        r, _r = gb(r, _r)
    else:
        break
    if len(set(tl)) == 1:
        r = (sum(tl) - m) // n
        break
print(r)
