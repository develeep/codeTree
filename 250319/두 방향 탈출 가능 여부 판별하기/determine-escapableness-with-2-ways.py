n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxy = ((1,0),(0,1))
def dfs(x,y):
    visited[x][y] = 1
    if x == (n-1) and y == (m-1):
        return 1
    c = 0
    for dx,dy in dxy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<n and 0<=ny<m):
            continue
        if visited[nx][ny] == 1 or grid[nx][ny] == 0:
            continue
        c += dfs(nx,ny)
    
    return c
visited = [[0]*m for _ in range(n)]
print(dfs(0,0))