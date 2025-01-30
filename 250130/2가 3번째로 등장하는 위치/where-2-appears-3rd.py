n = int(input())

arr = list(map(int,input().split()))

cnt = 0

for idx,num in enumerate(arr):
    if num == 2:
        cnt += 1
    if cnt==3:
        print(idx+1)
        break