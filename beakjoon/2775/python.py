from sys import stdin
m = []
def rd(a, b):
    while len(m) <= a:
        m.append([])
    while len(m[a]) <= b:
        m[a].append(-1)

    if m[a][b] != -1:
        return m[a][b]

    if a == 0:
        m[a][b] = b
        return b
    if b == 1:
        m[a][b] = 1
        return 1
    return rd(a-1, b) + rd(a, b-1)

t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    n = int(stdin.readline())

    r = rd(k, n)
    print(r)
