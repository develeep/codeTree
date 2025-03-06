n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
res = float('inf')
for i in range(n-1):
    for j in range(1, n):
        if arr[j] > (arr[i] + m):
            res = min(res, arr[j] - arr[i])
            break

print(res)