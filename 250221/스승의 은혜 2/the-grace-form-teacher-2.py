N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()

# Write your code here!
max_cnt = 0
for i in range(N):
    cnt = 0
    total = 0
    P[i] /= 2
    new_p = P[:]
    new_p.sort()
    for p in new_p:
        if total + p > B:
            break
        cnt += 1
        total += p            
    max_cnt = max(cnt,max_cnt)
    print()
    P[i] *= 2
    if cnt == N:
        break

print(max_cnt)
