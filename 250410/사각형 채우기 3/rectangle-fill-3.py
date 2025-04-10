n = int(input())

# Please write your code here.
DP = [0]*(n+4)

DP[0] = 1
DP[1] = 2

for i in range(2, n+1):
    DP[i] = (DP[i-1] * 2 + DP[i-2] * 3) % 1000000007
    for j in range(i-3,-1,-1):
        DP[i] = (DP[i] + DP[j]*2) % 1000000007

print(DP[n])
