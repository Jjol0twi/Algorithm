from sys import stdin
n, m = map(int, stdin.readline().split())
dic = {}
for _ in range(n):
    x = stdin.readline().strip()
    if len(x)<m:
        continue
    if not x in dic:
        dic[x] = 1
    else:
        dic[x] +=1
dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
print('\n'.join([item[0] for item in dic]))
