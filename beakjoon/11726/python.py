from sys import stdin

def fibonacci(n):
    if n == 1 or n==2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2])
    return dp[n]

n = int(stdin.readline())
print(fibonacci(n)%10007)
