n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1

for i in range(n):
    if i%2 == 0:
        for j in range(n-1,-1,-1):
            arr[j][n-i-1] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr[j][n-i-1] = cnt
            cnt += 1

for i in arr:
    print(*i)    
        