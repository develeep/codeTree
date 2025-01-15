n = int(input())

mul = 1
last = 0
for i in range(1, 10+1):
    mul *= i
    last = i
    if mul >= n:
        break

print(last)