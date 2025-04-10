n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
DP = [[float('inf')] * n for _ in range(n)]

import heapq

q = [(0,n-1,grid[0][n-1])]
DP[0][n-1] = grid[0][n-1]
dxy = ((1,0),(0,-1))
while q:
    x,y,m = heapq.heappop(q)
    DP[x][y] = m
    for dx, dy in dxy:
        nx,ny = x+dx,y+dy
        if not(0<=nx<n and 0<=ny<n):
            continue
        if DP[nx][ny] <= m + grid[nx][ny]:
            continue
        heapq.heappush(q,(nx,ny,m+grid[nx][ny]))

print(DP[n-1][0])