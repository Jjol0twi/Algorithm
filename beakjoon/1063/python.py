from sys import stdin

def chxy(a):
    if isinstance(a, str):
        x, y = list(a)
        return [ord(x) - 65, int(y)]
    elif isinstance(a, list):
        return f"{chr(a[0] + 65)}{a[1]}"

d = {
    "R": [1, 0], "L": [-1, 0], "B": [0, -1], "T": [0, 1], "RT": [1, 1], "LT": [-1, 1], "RB": [1, -1], "LB": [-1, -1]
}
k, s, n = map(lambda x: int(x) if x.isdigit() else x, list(stdin.readline().split()))
k, s = chxy(k), chxy(s)
for _ in range(int(n)):
    m = stdin.readline().strip()
    _k = [a + b for a, b in zip(k, d[m])]
    if not (0 <= _k[0] < 8 and 0 < _k[1] <= 8):
        continue
    if _k==s:
        _s = [a + b for a, b in zip(s, d[m])]
        if not (0 <= _s[0] < 8 and 0 < _s[1] <= 8):
            continue
        s = _s
    k = _k
print('\n'.join([chxy(k), chxy(s)]))
