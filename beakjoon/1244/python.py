from sys import stdin
sn = int(stdin.readline())
sw = list(map(int, stdin.readline().split()))
pn = int(stdin.readline())
for _ in range(pn):
    se, nu = map(int, stdin.readline().split())
    nu-=1
    if se%2==0:
        i = 0
        while sw[nu+i]==sw[nu-i]:
            sw[nu-i], sw[nu+i] = 1 if sw[nu-i]==0 else 0, 1 if sw[nu-i]==0 else 0
            i+=1
            if nu-i<0 or nu+i>=sn:
                break
    else:
        for i in range(nu, sn, nu+1):
            sw[i] = 1 if sw[i]==0 else 0
for i in range(0, len(sw), 20):
    print(*sw[i:i+20])
