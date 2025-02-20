X, Y = map(int, input().split())

# Write your code here!
cnt = 0
for i in range(X,Y+1):
    arr = []
    while i > 0:
        arr.append(i % 10)
        i //= 10
    s = list(set(arr))
    hap = sum(arr)
    len_arr = len(arr)
    if len(s) != 2:
        continue
    if (s[0]*(len_arr-1) + s[1]) == hap or (s[1]*(len_arr-1) + s[0]) == hap:
        cnt += 1 

print(cnt)