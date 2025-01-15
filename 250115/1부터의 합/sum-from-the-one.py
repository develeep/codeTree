n = int(input())
hap = 0
for i in range(1,100+1):
    hap += i
    if hap >= n :
        print(i)
        break