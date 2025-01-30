n = int(input())
cnt = 0
result = []

for i in range(n,n*10+1,n):
    result.append(i)
    if i % 5 == 0:
        cnt += 1
        if cnt == 2:
            break

for i in result:
    print(i,end=" ")