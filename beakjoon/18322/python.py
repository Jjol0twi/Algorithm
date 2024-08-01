import sys
n, k = map(int, sys.stdin.readline().split())
st = list(map(str, sys.stdin.readline().split()[:n]))
rs = [[st[0]]]
for i in range(1,len(st)):
    if len(''.join(rs[-1]))+len(st[i])<=k:
        rs[-1].append(st[i])
    else:
        rs.append([st[i]])
print('\n'.join([' '.join(rs[i]) for i in range(len(rs))]))
