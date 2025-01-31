arr = [list(map(int,input().split()))for _ in range(4)]
hap = 0

for i in range(4):
    for j in range(i+1):
        hap += arr[i][j]

print(hap)