n, k = map(int, input().split())

# Write your code here!
arr = [i for i in range(1,n+1)]
del_point = 0
del_arr = []
cnt = 0
while 1:
    if len(del_arr) == n:
        break
    if arr[del_point]:
        cnt += 1
    if cnt == k:
        del_arr.append(arr[del_point])
        arr[del_point] = 0
        cnt = 0
    del_point = (del_point+1) % n

print(*del_arr)