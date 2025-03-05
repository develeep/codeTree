n, m = map(int, input().split())
a = list(map(int, input().split()))
used = [0]*m
# Please write your code here.
a.sort()

for i in range(m-1,-1,-1):
    if len(a) == 0:
        break
    while 1:
        if len(a) == 0:
            break
        user = a.pop()
        if i >= user:
            used[i] = 1
            break

print(sum(used))