n = int(input())

for i in range(n,0,-1):
    for _ in range(i):
        print('*',end=" ")
    print()
for j in range(2,n+1):
    for _ in range(j):
        print('*',end=" ")
    print()