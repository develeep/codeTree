n = int(input())

for i in range(n,0,-1):
    for _ in range(i):
        for _ in range(i):
            print('*',end="") 
        print(end=" ")
    print()