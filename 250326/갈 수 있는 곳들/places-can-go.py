n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

dxy = ((0,1),(0,-1),(-1,0),(1,0))
def bfs():
    q = deque()
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for r,c in points:
        q.append((r-1,c-1))
        visited[r-1][c-1] = 1
    while q:
        r,c = q.popleft()
        cnt += 1
        for dx,dy in dxy:
            nx,ny = r + dx, c + dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if grid[nx][ny] or visited[nx][ny]:
                continue
            
            visited[nx][ny] = 1
            q.append((nx,ny))
    print(cnt)

bfs()
    