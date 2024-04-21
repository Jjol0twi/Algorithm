import sys
n = int(sys.stdin.readline())   # 입력 1
testimony = list(reversed(list(map(int, sys.stdin.readline().split()[:n]))))    # 입력 2 역순으로 변경
line = []
for i in range(n):
    line.insert(testimony[i], n-i)
print(' '.join(str(x) for x in line))
