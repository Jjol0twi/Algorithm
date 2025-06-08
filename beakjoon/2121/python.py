from sys import stdin
n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
nxy = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
result = 0

nxy_set = set(nxy)
for x, y in nxy:
    p1 = (x + a, y)     # 점 1
    p2 = (x, y + b)     # 점 2
    p3 = (x + a, y + b) # 점 3
    if p1 in nxy_set and p2 in nxy_set and p3 in nxy_set:   # 점 찾기
        result += 1
print(result)
