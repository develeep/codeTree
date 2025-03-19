n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
nodes = [[] for _ in range(n+1)]
# Please write your code here.
for start, end in edges:
    nodes[start].append(end)
    nodes[end].append(start)

dfs(1)