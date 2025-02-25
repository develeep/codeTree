n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
positions = [1]*k

max_result = 0
def find_max(idx):
    if idx == n:
        global max_result
        cnt = 0
        for pos in positions:
            if pos >= m:
                cnt += 1
        max_result = max(max_result,cnt)
        return
    move = nums[idx]
    for i in range(k):
        if positions[i] > m:
            continue
        
        positions[i] += move
        find_max(idx+1)
        positions[i] -= move
    else:
        cnt = 0
        for pos in positions:
            if pos >= m:
                cnt += 1
        max_result = max(max_result,cnt)
        return
        
find_max(0)
print(max_result)