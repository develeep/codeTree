arr = list(map(int,input().split()))
new_arr = []

for i in arr:
    if i == 0:
        break
    new_arr.append(i)

print(sum(new_arr),f'{sum(new_arr)/len(new_arr):.1f}')