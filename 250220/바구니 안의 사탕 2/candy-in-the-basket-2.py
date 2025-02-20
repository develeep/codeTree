N, k = map(int, input().split())
candy = [0]*101

for _ in range(N):
    c, p = map(int, input().split())
    candy[p] += c
# Write your code here!

max_result = float(0)
max_index = k
if k >= 101:
    max_result = sum(candy)
else:
    for i in range(k,102):
        left = max(0,i-k)
        right = min(102,i+k+1)
        c = sum(candy[left:right])
        max_result = max(max_result,c)

print(max_result)