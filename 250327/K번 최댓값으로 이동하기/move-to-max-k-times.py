n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque
dxy = ((0,1),(0,-1),(-1,0),(1,0))
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    max_height = grid[x][y]
    rs_x, rs_y = n,n
    res = 0
    flag = 1
    while q:
        x,y = q.popleft()
        if max_height > grid[x][y] > res:
            flag = 0
            rs_x,rs_y = x,y
            res = grid[x][y]
        if grid[x][y] == res:
            if x < rs_x:
                rs_x,rs_y = x,y
            elif x == rs_x and y < rs_y:
                rs_x,rs_y = x,y

        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            
            if visited[nx][ny] or grid[nx][ny] >= max_height:
                continue

            visited[nx][ny] = 1
            q.append((nx,ny))
    
    if flag:
        return -1,-1
    return rs_x,rs_y


mx,my = r-1, c-1
for _ in range(k):
    nx,ny = bfs(mx,my)
    if nx == -1:
        break
    mx,my = nx,ny

print(mx+1,my+1)