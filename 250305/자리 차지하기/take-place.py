n, m = map(int, input().split())
a = list(map(int, input().split()))
used = [0]*m
# Please write your code here.
def sit(user):
    for u in range(user-1,-1,-1):
        if used[u] == 0:
            used[u] = 1
            return 1
    return 0

for ar in a:
    if sit(ar) == 0:
        break


print(sum(used))