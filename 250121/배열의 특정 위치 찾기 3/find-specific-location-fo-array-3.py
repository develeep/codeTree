arr = list(map(int,input().split()))
new_arr = []
for i in arr:
    if i == 0:
        break
    new_arr.append(i)

print(new_arr[-1]+new_arr[-2]+new_arr[-3])