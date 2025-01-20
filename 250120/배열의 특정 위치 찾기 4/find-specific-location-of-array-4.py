arr = list(map(int,input().split()))
new_arr = []

for i in arr:
    if i == 0:
        break
    if i%2 == 0:
        new_arr.append(i)
    
print(len(new_arr),sum(new_arr))