N, k = map(int, input().split())
candy = [0]*101

for _ in range(N):
    c, p = map(int, input().split())
    candy[p] += c
# Write your code here!

max_result = float('-inf')
max_index = k
for i in range(k,102-k):
    c = sum(candy[i-k:i+k+1])
    max_result = max(max_result,c)

print(max_result)