from sys import stdin
input = stdin.readline

def flip(matrix, k, q):
    for i in range(k, k+3):
        for j in range(q, q+3):
            if matrix[i][j] == '0':
                matrix[i][j] = '1'
            else:
                matrix[i][j] = '0'
    return matrix

n, m = map(int, input().split())
a = [list(input().strip()[:m]) for _ in range(n)]
b = [list(input().strip()[:m]) for _ in range(n)]
if a==b:
    print(0)
    exit()
if n < 3 or m <3:
    print(-1)
    exit()
result = 0
_a = a
for i in range(n-2):
    for j in range(m-2):
        if _a[i][j]!=b[i][j]:
            _a = flip(_a,i,j)
            result+=1
if a==b:
    print(result)
else:
    print(-1)
