import sys
import re
input = sys.stdin.readline
for _ in range(int(input())):
    rs = input()
    ac = []
    for l in sys.stdin:
        if l.strip() == 'what does the fox say?':
            break
        ac.append(l.split()[-1])
    rs =re.sub(r'\b(?:' + '|'.join(re.escape(word) for word in ac) + r')\b', '', rs).strip()
    print(re.sub(r'\s+', ' ', rs))
