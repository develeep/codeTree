N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()

# Write your code here!
max_cnt = 0
for i in range(N):
    cnt = 0
    max_price = B
    for p in P:
        if p == P[i]:
            p //= 2
        if max_price - p < 0:
            break
        cnt += 1
        max_price -= p
            
    max_cnt = max(cnt,max_cnt)
    if cnt == N:
        break

print(max_cnt)