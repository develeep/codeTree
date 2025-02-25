n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
positions = [1]*k

max_result = 0
def find_max(idx):
    global max_result
    if max_result == k:
         return
    if idx == n:
        cnt = 0
        for pos in positions:
            if pos >= m:
                cnt += 1
        max_result = max(max_result,cnt)
        return

    flag = 0
    move = nums[idx]
    for i in range(k):
        if positions[i] > m:
            continue
        flag = 1       
        positions[i] += move
        find_max(idx+1)
        positions[i] -= move
        
    if flag == 0:
        max_result = k
        return
        
find_max(0)
print(max_result)