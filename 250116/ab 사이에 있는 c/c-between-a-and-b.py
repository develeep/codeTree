a,b,c = map(int,input().split())
is_c = 0

for i in range(a,b+1):
    if i%c == 0 :
        is_c = 1
        break

print('YES' if is_c else 'NO')