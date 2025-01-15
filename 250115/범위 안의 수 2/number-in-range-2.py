hap,cnt = 0,0

for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        hap+=n
        cnt+=1
    
print(hap,f'{hap/cnt:.1f}')