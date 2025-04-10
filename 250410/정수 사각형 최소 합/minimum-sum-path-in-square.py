n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
DP = [[float('inf')] * n for _ in range(n)]

import heapq
dxy = ((1,0),(0,-1))
D = [[float('inf')]*n for _ in range(n)]

def f(x,y):
    q = [(grid[x][y],x,y)]
    while q:
        m,x,y = heapq.heappop(q)
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy

            if (nx,ny) == (n-1,0):
                return m + grid[nx][ny]
            if not(0<=nx<n and 0<=ny<n):
                continue
            move = m + grid[nx][ny]
            if move < D[nx][ny]:
                D[nx][ny] = move
                heapq.heappush(q, (move,nx,ny))

print(f(0,n-1))