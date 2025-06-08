from sys import stdin
n = int(stdin.readline())   # 6
input = [int(stdin.readline()) for _ in range(n)]   # [10, 20, 15, 25, 10, 20]
dp = [input[0]] * (n - 2)

for i in range(1, n - 1):  # 0 ~ (n-1)
    for j in range(1, i):
            dp[i]

# result = 0
# i = 0
# while i < (n-1):
#     if (i+1) >= (n-1):
#         result += input[i]
#         break
#     print(result,input[i],input[i+1])
#     result += max(input[i],input[i+1])
#     if input[i] < input[i+1]:
#         i+=2
# print(result+input[-1])
