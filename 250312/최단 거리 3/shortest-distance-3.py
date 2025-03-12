import heapq
def bfs(start):
    q = [(0, start)]
    visited = [0]*(n+1)
    min_depth = [100000]*(n+1)
    min_depth[start] = 0
    while q:
        depth, node = heapq.heappop(q)
        if node == B:
            return depth
        for neighbor, length in nodes[node]:
            m = depth + length
            if min_depth[neighbor] > m:
                min_depth[neighbor] = m
                heapq.heappush(q, (m, neighbor))
    return False


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
nodes = [set() for _ in range(n+1)]
for start, end, length in edges:
    nodes[start].add((end, length))
    nodes[end].add((start, length))



print(bfs(A))        