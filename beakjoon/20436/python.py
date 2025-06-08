from sys import stdin
kw = [["z","x","c","v"],["a","s","d","f","g"],["q","w","e","r","t"],["b","n","m"],["h","j","k","l"],["y","u","i","o","p"]]

def now_index(gw):
    for k, s in enumerate(kw):
        if gw in s:
            return (k, s.index(gw))

def xy_dif(a, b):
    _r = 0
    if a[0]//3 != b[0]//3:
        _r += abs(a[0]-b[0])
        if a[0]==0:
            _r += (len(kw[a[0]])-a[0])+b[0]
        else:
            _r += abs(a[1]-b[1])
    else:
        for c, d in zip(a, b):
            _r += abs(c-d)
    return _r

nl, nr = map(str, stdin.readline().split())
smw = list(stdin.readline().strip())
r = 0
for i in smw:
    x, y, j = now_index(nl), now_index(nr), now_index(i)
    if j[0] // 3 == 1:
        r+=xy_dif(y, j)
        nr = i
    else:
        r+=xy_dif(x, j)
        nl = i
    r+=1
print(r)
