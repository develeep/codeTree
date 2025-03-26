n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque

dxy = ((1,0),(-1,0),(0,1),(0,-1))
def bfs(x,y):
    max_num = grid[x][y]
    q = deque()
    q.append((x,y))
    res_x,res_y = 0,0
    res = 0
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dxy:
            nx,ny = x + dx, y + dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            
            if grid[nx][ny] >= max_num or visited[nx][ny]:
                continue
            
            if res < grid[nx][ny]:
                res_x, res_y = nx,ny
                res = grid[nx][ny]
            
            if res == grid[nx][ny]:
                if res_x > nx:
                    res_x, res_y = nx,ny
                elif res_x == nx and res_y > ny:
                    res_x, res_y = nx,ny
            
            visited[nx][ny] = 1
            q.append((nx,ny))
    return (res_x,res_y)

res_x, res_y = r-1,c-1
for _ in range(k):
    rx, ry = bfs(res_x,res_y)

    if rx == ry == 0:
        break
    res_x,res_y = rx,ry

print(res_x+1,res_y+1)