n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

def bfs():
    q = deque()
    for r,c in points:
        q.append((r,c,0))