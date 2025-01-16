a,b,c = map(int,input().split())
result = 'YES'
for i in range(a,b+1):
    if i % c == 0:
        result = 'NO' 
        break

print(result)
