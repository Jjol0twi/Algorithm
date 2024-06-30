from sys import stdin
n, k = map(int, stdin.readline().strip().split())
s = list(stdin.readline().strip())
rs = s[:(k-1)]
del s[:(k-1)]
if (n-k)%2==0:
    rs.reverse()
print(''.join([*s,*rs]))
