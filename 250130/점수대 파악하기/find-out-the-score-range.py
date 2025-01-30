arr = list(map(int,input().split()))

result = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(arr)):
    if arr[i] == 0 : 
        break
    if arr[i] >= 10:
        result[arr[i]//10-1] += 1

for i in range(9,-1,-1):
    print(f'{i+1}0 - {result[i]}')