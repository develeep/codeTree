n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
dxy = ((-1,0),(1,0),(0,1),(0,-1))
def check(x,y):
    cnt = 0
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not(0<=nx<n and 0<=ny<m):
            continue

        if not a[nx][ny]: 
            return 0
    return 1           
def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if not a[i][j]:
                q.append((i,j,0))
    
    res = 0
    dep = 0
    while q:
        x,y,depth = q.popleft()
        if depth > dep:
            print(*a,sep='\n')
            print()
            dep = depth
            res = 0
        res += 1
        # print(dep,res)
        

        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<m):
                continue
            if a[nx][ny] == 0:
                continue
            a[nx][ny] = 0
            q.append((nx,ny, depth+1))
    return dep, res
print(bfs())