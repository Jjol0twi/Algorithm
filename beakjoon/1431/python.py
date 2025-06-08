import sys
import re
n = int(sys.stdin.readline())
l = list(str(sys.stdin.readline().strip()) for _ in range(n))
l.sort(key=lambda x: (len(x), sum(int(n) for n in re.findall(r'\d',x)), x ))
print('\n'.join(l))
