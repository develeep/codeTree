n,m = map(int,input().split())

arr = [[0 for _ in range(m)]for _ in range(n)]
cnt = 1

for i in range(m):
    for j in range(i+1 if i < n else n):
        arr[j][i-j] = cnt
        cnt +=1

for i in range(1,n):
    max_cnt = 0
    for j in range(i,n):
        max_cnt += 1
        arr[j][m-max_cnt] = cnt
        cnt += 1
        if max_cnt == m :
            break




for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()

