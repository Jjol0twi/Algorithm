import sys
t = int(sys.stdin.readline())
tc = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
for i in range(t):
    print(f"Case #{i+1}: {tc[i][0]} + {tc[i][1]} = {sum(tc[i])}")
