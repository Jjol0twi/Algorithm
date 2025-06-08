from sys import stdin
n = int(stdin.readline())
l = set()
for _ in range(n):
    p, s = map(str, stdin.readline().split())
    if s == "enter":
        l.add(p)
    else:
        l.discard(p)
print('\n'.join(sorted(l, reverse=True)))
