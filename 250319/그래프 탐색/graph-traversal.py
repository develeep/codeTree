n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
nodes = [[] for _ in range(n+1)]
# Please write your code here.
def dfs(node):
    visited[node] = 1
    c = 1
    for neighbor in nodes[node]:
        if visited[neighbor] == 1:
            continue
        c += dfs(neighbor)
    return c

for start, end in edges:
    nodes[start].append(end)
    nodes[end].append(start)
visited = [0]*(n+1)
print(dfs(1)-1)