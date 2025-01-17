n = int(input())
cnt = 1

for i in range(n):
    for _ in range(i):
        print(' ',end=" ")
    for _ in range(n-i):
        print(cnt,end=" ")
        if cnt == 9:
            cnt = 1
            continue
        cnt+=1
    print()