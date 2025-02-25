n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!

def find_max(idx,cnt,val):
    if idx == n:
        return

    if cnt == m:
        global max_result
        max_result = max(max_result, val)
        return

    find_max(idx+1,cnt,val)

    find_max(idx+1,cnt+1,val^A[idx])

max_result = float('-inf')
find_max(0,0,0)

print(max_result)