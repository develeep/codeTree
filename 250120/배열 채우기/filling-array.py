arr =list(map(int,input().split()))
new_arr = []

for i in  range(len(arr)):
    if arr[i] == 0:
        new_arr = arr[:i]
        break
    new_arr.append(arr[i])

for i in new_arr[::-1]:
    print(i,end=" ")
