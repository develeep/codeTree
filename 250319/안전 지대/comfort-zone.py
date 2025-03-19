n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
safe = [[1]*m for _ in range(n)]
# Please write your code here.
max_height = max([s for ar in grid for s in ar])

def fill(k):
    for i in range(n):
        for j in range(m):
            if not safe[i][j]:
                continue
            if grid[i][j] <= k:
                safe[i][j] = 0

dxy = ((0,1),(0,-1),(1,0),(-1,0))
def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in dxy:
        nx,ny = x+dx, y+dy
        if not(0<=nx<n and 0<=ny<m):
            continue
        if visited[nx][ny] or not safe[nx][ny]:
            continue
        dfs(nx,ny)


res = 1
res_cnt = 0
for i in range(1,max_height+1):
    fill(i)
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if safe[x][y] and not visited[x][y]:
                cnt += 1
                dfs(x,y)
    if cnt > res_cnt:
        res_cnt = cnt
        res = i
print(res,res_cnt)