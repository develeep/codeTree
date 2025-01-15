n = int(input())

cnt= 0

for i in range(1,100):
    n /=i
    cnt+=1
    if 1 >= n:
        break

print(cnt)