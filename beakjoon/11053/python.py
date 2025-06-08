from sys import stdin

n = int(stdin.readline())
input = list(map(int, stdin.readline().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if input[j] < input[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
