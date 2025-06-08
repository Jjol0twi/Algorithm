import sys
from collections import Counter

def list_difference(l, f):
    c1 = Counter(l)
    c2 = Counter(f)
    dc = c1 - c2
    result = list(dc.elements())
    return result

n = int(sys.stdin.readline())
l = [str(sys.stdin.readline().strip()) for _ in range(n)]
f = [str(sys.stdin.readline().strip()) for _ in range(n-1)]
print('\n'.join(list_difference(l,f)))
