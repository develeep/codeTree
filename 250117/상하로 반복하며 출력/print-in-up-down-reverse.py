n = int(input())
cnt = 1
arr = []

for i in range(n):
    arr2 = []
    for j in range(n):
        arr2.append(j)
    arr.append(arr2)

for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        
        if i % 2 == 1:
            if cnt == 1:
                continue
            cnt -= 1
        else : 
            if cnt % n == 0:
                continue
            cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end="")
    print()