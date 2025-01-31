n = int(input())

arr = list(map(int,input().split()))

result = 100

for i in range(n-1):
    x = arr[i+1] - arr[i]
    if x == 1:
        result = x
        break
    if x > result:
        result = x
    
print(result)