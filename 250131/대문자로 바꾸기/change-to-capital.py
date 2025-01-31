arr = []
for i in range(5):
    arr.append(input().split())

    for j in range(3):
        print(arr[i][j].upper(),end=" ")
    print()