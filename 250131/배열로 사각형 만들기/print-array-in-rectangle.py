arr = [[0 for _ in range(5)]for _ in range(5)]

for i in range(5):
    cnt = 1
    plus = i
    plus2 = 6
    for j in range(5):
        arr[i][j] = cnt
        if i == 1:
            cnt += 1
        elif i == 2:
            cnt += i + j
        elif i == 3:
            cnt += plus
            plus += i + j
        elif i == 4:
            cnt += plus
            plus += plus2 
            plus2 += i+j
            
for i in arr:
    print(*i)