n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
visited = [0]*n
max_result = 0
def find_max(arr,m_cnt,move_cnt):
    global max_result
    if max_result >= k:
        return
    if len(arr) == n:
        if move_cnt >= m:
            m_cnt += 1
        max_result = max(max_result,m_cnt)
        return
    for i in range(n):
        if max_result >= k:
            return
        if visited[i] == 0:
            visited[i] = 1
            if move_cnt >= m:
                find_max(arr + [nums[i]], m_cnt+1, 1 + nums[i])
            else:
                find_max(arr + [nums[i]], m_cnt, move_cnt + nums[i])
            visited[i] = 0

find_max([],0,1)
print(max_result)
