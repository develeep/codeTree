n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dx = [[1,-1,0,0],[1,1,-1,-1],[1,2,-1,-2]]
dy = [[0,0,1,-1],[1,-1,1,-1],[0,0,0,0]]

xy_arr = []

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            xy_arr.append((i,j))

max_result = 0

def find_max(i):
    if i == len(xy_arr):
        return 0
    x,y = xy_arr[i]
    idx = 0
    m_cnt = 0

    for d in range(3):
        cnt = 0


        for d_idx in range(4):
            nx = x + dx[d][d_idx]
            ny = y + dy[d][d_idx]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                cnt += 1
                grid[nx][ny] = i+2


        c = cnt + find_max(i+ 1)
        m_cnt = max(m_cnt,c)


        for d_idx in range(4):
            nx = x + dx[d][d_idx]
            ny = y + dy[d][d_idx]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == i+2:
                grid[nx][ny] = 0
    return m_cnt

max_result = find_max(0) + len(xy_arr)
print(max_result)