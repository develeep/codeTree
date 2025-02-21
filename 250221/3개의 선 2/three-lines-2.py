n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Write your code here!
line = []
def find(index):
    if len(line) >= n:
        return len(set(line)) == 3
    
    line.append(('x',x[index]))
    if find(index+1):
        return True
    line.pop()

    line.append(('y',y[index]))
    if find(index+1):
        return True
    line.pop()

    return False

print(int(find(0)))