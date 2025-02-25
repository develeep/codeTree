n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def find_min(cnt,cost):
    if cnt == n:
        global min_result
        total = 0
        for i in range(n-1,0,-1):
            a = A[cost[i]][cost[i-1]]
            if a == 0:
                return
            total += a
        last = A[cost[-1]][0]
        if last == 0:
            return
        total += last
        min_result = min(min_result,total)
    
    for i in range(1,n):
        if visited[i] == 0:
            visited[i] = 1
            find_min(cnt+1,cost+[i])
            visited[i] = 0

min_result = float('inf')
visited = [0]*n
find_min(1,[0])

print(min_result)
