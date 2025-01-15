a,b = map(int,input().split())
hap = 0

if a >= b:
    for i in range(b,a+1):
        if i % 5 == 0:
            hap += i

if a < b:
    for i in range(a,b+1):
        if i % 5 == 0:
            hap += i

print(hap)

