n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        print(cnt,end=" ")
        if j == n-1:
            cnt += n
            continue
        if i % 2 == 0:
            cnt += 1
        else : 
            cnt -= 1
    print()