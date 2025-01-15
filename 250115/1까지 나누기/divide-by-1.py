n = int(input())

cnt= 0

for i in range(1,1000):
    n //= i
    cnt+=1
    if 1 >= n:
        break

print(cnt)