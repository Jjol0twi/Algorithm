import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()[:n]))
tl = []
nn = 1
while len(l)!=0 or len(tl)>=1:
    if len(l)!=0 and l[0]==nn:
        del l[0]
        nn+=1
        continue
    if len(tl)!=0 and tl[-1]==nn:
        del tl[-1]
        nn+=1
        continue
    if len(l)==0 and tl[-1]!=nn:
        print("Sad")
        break
    tl.append(l.pop(0))
if len(l)==0 and len(tl)==0:
    print("Nice")
