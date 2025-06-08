from sys import stdin
from decimal import Decimal
n, k = map(int, stdin.readline().strip().split())
gl = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
for i in range(n):
    gl[i][2] = Decimal(gl[i][2])/Decimal(gl[i][1])
gl.sort(key = lambda x : [ -x[2] , x[1], x[0]])
for i in range(k):
    print(gl[i][0])
