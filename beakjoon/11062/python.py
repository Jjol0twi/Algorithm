import sys

input = sys.stdin.readline

def getMaxScore(n, cards):
    dp = [[0] * n for _ in range(n)]
    prefix_sum = [0] * (n + 1)  #
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + cards[i]

    for i in range(n):
            dp[i][i] = cards[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = prefix_sum[j + 1] - prefix_sum[i]
            dp[i][j] = max(
                total - dp[i+1][j],
                total - dp[i][j-1]
            )
    return dp[0][n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    print(getMaxScore(n, cards))
