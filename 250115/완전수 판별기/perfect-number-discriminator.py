n =  int(input())
hap

for i in range(1,n):
    if (n%i == 0):
        hap += i

print('P' if hap == n else 'N')