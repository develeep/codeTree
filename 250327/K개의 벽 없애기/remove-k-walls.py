from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

wall = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            wall.append((i,j))
dxy = ((-1,0),(1,0),(0,1),(0,-1))
# Please write your code here.
def bfs(arr):
    for x,y in arr:
        grid[x][y] = 0

    q = deque()
    q.append((r1,c1,0))
    visited = [[0]*n for _ in range(n)]
    visited[r1][c1] = 1
    while q:
        x,y,depth = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] or grid[nx][ny]:
                continue
            if (nx,ny) == (r2,c2):
                for x,y in arr:
                    grid[x][y] = 1
                return depth + 1
            visited[nx][ny] = 1
            q.append((nx,ny,depth+1))

    for x,y in arr:
        grid[x][y] = 1
    return -1

res = float('inf')
def f(arr):
    global res
    if len(arr) == k:
        r = bfs(arr)
        if r > -1:
            res = min(res,r)
        return

    for i in range(len(wall)):
        if used[i]:
            continue
        used[i] = 1
        f(arr + [(wall[i][0],wall[i][1])])
        used[i] = 0

used = [0]*8
f([])
if res == float('inf'):
    res = -1

print(res if (r1,c1) != (r2,c2) else 0)