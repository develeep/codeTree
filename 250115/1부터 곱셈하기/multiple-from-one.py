n = int(input())
mul = 1
for i in range(1, 10):
    mul *= i
    if mul >= n:
        print(i)
        break