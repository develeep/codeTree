arr = list(map(int,input().split()))


for i in range(2,10):
    n = arr[i-1] + arr[i-2]*2
    arr.append(n)

for i in arr:
    print(i,end=" ")