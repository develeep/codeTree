arr = list(map(int,input().split()))

sum1 = sum(arr[::2])
sum2 = sum(arr[1::2])

print(sum1 - sum2 if sum1 > sum2 else sum2 - sum1)
