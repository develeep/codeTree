n = [0,0,0,0]

for _ in range(3):
    i = input().split()
    if i[0] == 'Y':
        if int(i[1]) >= 37:
            n[0] += 1 
            continue
        n[2] += 1
        continue
    if int(i[1]) >= 37:
            n[1] += 1 
            continue
    n[3] += 1

for i in n:
    print(i,end=" ")

if n[0] >= 2:
    print('E')

