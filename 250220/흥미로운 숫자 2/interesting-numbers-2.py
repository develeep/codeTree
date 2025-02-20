X, Y = map(int, input().split())

# Write your code here!
cnt = 0
for i in range(X,Y+1):
    arr = [n for n in str(i)]
    s = set(arr)
    if len(s) == 2:
        dir = {}
        for S in s:
            dir[S] = 0
        for a in arr:
            dir[a] += 1
        for i in dir:
            if dir[i] == 1:
                cnt += 1

print(cnt)