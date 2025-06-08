import sys
while True:
    a = sys.stdin.readline().strip()
    if a=="0":
        break
    if a[:(len(a)//2)]==a[::-1][:(len(a)//2)]:
        print("yes")
    else:
        print("no")
