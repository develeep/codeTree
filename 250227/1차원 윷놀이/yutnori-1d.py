n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
result = 0
def f(i,moves):
    if i >= n:
        global result
        c = list(filter(lambda x: x >= m, moves))
        result = max(result, len(c))
        return

    for idx in range(k):
        if moves[idx] >= m and idx < k-1:
            continue
        moves[idx] += nums[i]
        f(i+1,moves)
        moves[idx] -= nums[i]


f(0,[1]*k)
print(result)