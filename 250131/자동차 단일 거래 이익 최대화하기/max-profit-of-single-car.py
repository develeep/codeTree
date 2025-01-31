n = int(input())
arr = list(map(int,input().split()))
result = 0


for i in range(n-1):
    for j in range(i+1,n):
        x = arr[j] - arr[i]
        if x > result:
            result = x

print(result)