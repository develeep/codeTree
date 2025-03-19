n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxy = ((0,1),(0,-1),(-1,0),(1,0))
def dfs(x,y):
    c = 1
    grid[x][y] = 0
    for dx,dy in dxy:
        nx,ny = x+dx, y+dy
        if not (0<=nx<n and 0<=ny<n):
            continue
        if not grid[nx][ny]:
            continue
        c += dfs(nx,ny)
    return c
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            cnt += 1
            res.append(dfs(i,j))

res.sort()
print(cnt)
print('\n'.join(map(str,res)))
