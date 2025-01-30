n = int(input())
idx = 2
result = [1,n]

while 1:
    n = result[idx-2] + result[idx-1]
    result.append(n)
    idx += 1
    if n >= 100:
        break

for i in result:
    print(i,end=" ")