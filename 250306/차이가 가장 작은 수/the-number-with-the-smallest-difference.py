n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
res = float('inf')
for i in range(n-1):
    for j in range(1, n):
        if abs(arr[i] - arr[j]) >= m:
            res = min(res,abs(arr[i]-arr[j]))
            break
print(res if res < float('inf') else -1)
