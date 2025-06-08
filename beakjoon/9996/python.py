from sys import stdin
import re

n = int(stdin.readline())
p = stdin.readline().strip()
fn = [stdin.readline().strip() for _ in range(n)]
p = p.replace("*",".*")
rp = re.compile(f"^{p}$")
for i in range(n):
    if rp.match(fn[i]):
        print("DA")
    else:
        print("NE")
