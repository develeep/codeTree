a,b = map(int,input().split())

for i in range(1,a+1):
    for j in range(i,i*b+1,i):
        print(j,end=" ")
    print()