n = int(input())

arr = list(map(int,input().split()))

result = [0,0,0,0,0,0,0,0,0]

for i in range(len(arr)):
    result[arr[i]-1] += 1

for i in result:
    print(i)