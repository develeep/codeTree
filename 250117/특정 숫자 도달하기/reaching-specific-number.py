arr = list(map(int,input().split()))
result_arr = []
for i in arr:
    if i < 250:
        result_arr.append(i)
    else:
        break
print(sum(result_arr),f'{sum(result_arr)/len(result_arr):.1f}')
        