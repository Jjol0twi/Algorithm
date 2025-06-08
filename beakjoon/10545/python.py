import sys
ke = [[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
ch = list(map(int, sys.stdin.readline().split()[:9]))
st = list(sys.stdin.readline().strip())
bu = {i : ke[ch[i]-1] for i in range(9)}
re = ""
for i in range(len(st)):
    for j in range(9):
        if st[i] in bu[j]:
            x = str(j+1)
            if len(re) != 0 and re[-1] == x:
                re+="#"
            y = bu[j].index(st[i])+1
            re += x*y
print(re)
