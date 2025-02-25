n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
visited = [0]*n
max_result = 0
def find_max(arr):
    global max_result
    if max_result >= k:
        return
    if len(arr) == n:
        cnt = 0
        move_cnt = 1
        for move in arr:
            move_cnt += move
            if move_cnt >= m:
                cnt += 1
                move_cnt = 1
        max_result = max(max_result,cnt)
        return
    for i in range(n):
        if max_result >= k:
            break
        if visited[i] == 0:
            visited[i] = 1
            find_max(arr + [nums[i]])
            visited[i] = 0

find_max([])
print(max_result)