n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

# Please write your code here.
def find_p(v):
    if v != nodes[v]:
        nodes[v] = find_p(nodes[v])
    return nodes[v]

nodes = list(range(n+1))
rank = [1]*(n+1)

for op, *nums in operations:
    if op == "x":
        pa = find_p(nums[0])
        pb = find_p(nums[1])
        if pa == pb:
            continue
        if pa < pb:
            nodes[pb] = pa
        else:
            nodes[pa] = pb
    else:
        cnt = 0
        for node in nodes:
            if node == nodes[nums[0]]:
                cnt += 1 
        print(cnt)