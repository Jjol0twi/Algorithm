import sys
n = int(sys.stdin.readline())
max = 0
err = 0
while(n!=0):
    input = sys.stdin.readline()
    if input=="\n":
        per = round(100 - (err / max * 100),1)
        print("Efficiency ratio is {:g}%.".format(per))
        max = 0
        err = 0
        n-=1
        continue
    max+=len(input.strip())
    err+=input.count("#")
