n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def find_min(idx,cnt,cost):
    if cnt == n:
        global min_result
        if A[idx][0] == 0:
            return
        cost += A[idx][0]
        min_result = min(min_result,cost)
    
    for i in range(1,n):
        if A[idx][i] == 0:
            continue
        if visited[i] == 0:
            visited[i] = 1
            find_min(i,cnt+1,cost+A[idx][i])
            visited[i] = 0

min_result = float('inf')
visited = [0]*n
find_min(0,1,0)

print(min_result)