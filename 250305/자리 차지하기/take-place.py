n, m = map(int, input().split())
a = list(map(int, input().split()))
used = [0]*m
# Please write your code here.
a.sort(reverse=True)

for i in range(m):
    if len(a) == 0:
        break
    while 1:
        if len(a) == 0:
            break
        user = a.pop()
        if i+1 <= user:
            used[i] = 1
            break

print(sum(used))