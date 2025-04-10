n = int(input())

# Please write your code here.
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 1
i = 3
while i < n:
    dp[i] = dp[i-2] + dp[i-3]
    i+= 1

print(dp[n-1])