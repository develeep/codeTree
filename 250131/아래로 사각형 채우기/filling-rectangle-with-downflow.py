n = int(input())

arr = [[i + j for i in range(1,j+1+(n*(n-1))+1,n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()