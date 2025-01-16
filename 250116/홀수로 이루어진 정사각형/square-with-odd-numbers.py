n = int(input())

for i in range(11,2*n+11,2):
    for j in range(i,i+2*n,2):
        print(j,end=" ")
    print()