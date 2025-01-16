a,b = map(int,input().split())
n = 0

for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        n = 1
        break

print(n)