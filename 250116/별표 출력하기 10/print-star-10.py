n = int(input())
x,y = 1, n

for i in range(1,n*2+1):
    if i % 2 == 1:
        for _ in range(x):
            print('*',end=" ")
        x += 1
    elif i % 2 == 0:
        for _ in range(y):
            print('*',end=" ")
        y -=1

    print()