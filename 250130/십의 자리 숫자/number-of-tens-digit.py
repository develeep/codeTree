arr = list(map(int,input().split()))

result = [0,0,0,0,0,0,0,0,0]

for i in range(len(arr)):
    if arr[i] == 0:
        break
    if arr[i] > 9:
        result[arr[i]//10-1] += 1

for i in range(9):
    print(f'{i+1} - {result[i]}')
    