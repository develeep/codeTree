n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!

def find_max(idx,cnt,val):
    if cnt == m:
        global max_result
        max_result = max(max_result, val)
        return

    if idx == n:
        return

    find_max(idx+1,cnt,val)

    find_max(idx+1,cnt+1,val^A[idx])

max_result = 0
find_max(0,0,0)

print(max_result)
