from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    if n == 1 or m == 1:    # 1이면 그냥 가져가면 끝나기에 예외 처리
        print("YES")
        continue
    if (n+m) % 2 != 0:      # rms
        print("YES")
    else:
        print("NO")
