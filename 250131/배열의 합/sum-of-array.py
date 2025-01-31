arr = []

for _ in range(4):
    arr.append(list(map(int,input().split())))

    
for i in range(4):
    print(sum(arr[i]))