import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
if(v>=a):
    print( math.ceil((v - a) / (a - b)) + 1)
else:
    print(1)
