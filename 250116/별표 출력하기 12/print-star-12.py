n = int(input())
for i in range(n):
    if i == 0:
        for _ in range(n):
            print('*', end=" ")
        print()
        continue
    for j in range(n):
        if j % 2 == 1:
            if j >= i:
                print('*', end=" ")
                continue
        print(' ', end=" ")
    print()