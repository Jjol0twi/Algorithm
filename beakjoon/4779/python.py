def tSplit(a):
    if len(a)==1:
        return a
    b = len(a)//3
    return tSplit(a[:b]) + (" "*b) + tSplit(a[:b])
r = None
while True:
    try:
        n = int(input())
        ln = n**3
        if r is not None and len(r) > ln:
            print(r[:ln])
        else:
            l = "-"*ln
            r = tSplit(l)
            print(r)
    except EOFError:
        break
