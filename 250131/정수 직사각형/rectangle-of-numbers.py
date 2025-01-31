n, m = map(int,input().split())
arr = [[i+(j*m) for i in range(1,m+1)] for j in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()