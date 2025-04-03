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
def count_node(num):
    cnt = 1
    visited = [0]*(n+1)
    visited[num] = 1
    stack = [num]
    while stack:
        num = stack.pop()
        for neighbor in nodes[num]:
            if visited[neighbor]:
                continue
            visited[neighbor] = 1
            stack.append(neighbor)
            cnt += 1
    return cnt

nodes = [[] for _ in range(n+1)]
for op, *nums in operations:
    if op == "x":
        nodes[nums[0]].append(nums[1])
        nodes[nums[1]].append(nums[0])
    else:
        print(count_node(nums[0]))        