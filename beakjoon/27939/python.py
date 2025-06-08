import sys
n = int(sys.stdin.readline())
v = list(map(str, sys.stdin.readline().split()))
m, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split()[:k])) for _ in range(m)]
na = [[v[a[i][j]-1] for j in range(k)] for i in range(m)]
re = ""
for i in range(m):
    if 'P' not in na[i]:
        re = "W"
if re == "":
    re = "P"
print(re)
