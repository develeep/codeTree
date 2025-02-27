n = int(input())

# Write your code here!
def check(arr):
    if len(arr) == n:
        print(*arr)
        return
    
    for i in range(n,0,-1):
        if visited[i] == 0:
            visited[i] = 1
            check(arr + [i])
            visited[i] = 0
            

visited = [0]*(n+1)

check([])
