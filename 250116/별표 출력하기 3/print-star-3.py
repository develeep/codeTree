n = int(input())
x = 2*(n-1)+1
blank = 0

for i in range(x,0,-2):
    for _ in range(blank):
        print(' ',end=" ")
    for _ in range(i):
        print('*',end=" ")
    blank += 1
    print()
