n = int(input())
cnt = 0
for _ in range(n):
    arr = list(map(int,input().split()))

    avr = sum(arr) / len(arr)

    if avr >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')

print(cnt)