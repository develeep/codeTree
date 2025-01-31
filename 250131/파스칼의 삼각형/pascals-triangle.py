n = int(input())

arr = [[1 for i in range(j+1)]for j in range(n)]

for i in range(2,n):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in arr:
    print(*i)