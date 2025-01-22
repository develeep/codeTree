arr = list(map(int,input().split()))

for i in range(2,10):
    x = arr[i-2] + arr[i-1]
    x %= 10
    arr.append(x)

for i in arr:
    print(i,end=" ")