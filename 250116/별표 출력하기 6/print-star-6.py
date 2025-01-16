n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ", end =" ")
    for _ in range(((n)*2-1)-i*2):
        print('*',end=" ")
    print()

for i in range(n-1):
    for _ in range(n-2-i):
        print(' ',end=" ")
    for _ in range((i+1)*2+1):
        print('*', end=" ")
    print()