n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*n for _ in range(n)]
max_size = max([s for ar in grid for s in ar])
max_cnt = 0
res = 0
dxy = ((0,1),(0,-1),(-1,0),(1,0))
def dfs(x,y, k):
    stack = [(x,y)]
    visited[x][y] = 1
    cnt = 0
    while stack:
        x,y = stack.pop()
        cnt += 1
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] or grid[nx][ny] != k:
                continue
            
            visited[nx][ny] = 1
            stack.append((nx,ny))
    return cnt

for k in range(1,max_size+1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == k and visited[i][j] == 0:
                cnt = dfs(i,j,k)
                max_cnt = max(max_cnt, cnt)
                if cnt >= 4:
                    res += 1

print(res, max_cnt)