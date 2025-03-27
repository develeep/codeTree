n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
from collections import deque
dxy = ((-1,-2),(-1,2),(1,2),(1,-2),(-2,-1),(-2,1),(2,1),(2,-1))

def bfs(x,y):
    q = deque()
    q.append((x,y,0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,depth = q.popleft()

        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if (nx,ny) == (r2-1,c2-1):
                return depth + 1
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append((nx,ny,depth + 1))
    return -1
print(bfs(r1-1,c1-1) if (r1,c1) != (r2,c2) else 0)