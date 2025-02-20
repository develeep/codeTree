X, Y = map(int, input().split())

# Write your code here!
cnt = 0
for i in range(X,Y+1):
    s = set([n for n in str(i)])
    if len(s) == 2:
        cnt += 1

print(cnt)