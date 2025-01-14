n = int(input())

def find3(i):
    if i % 10 == 0:
        return False
    if (i % 10 )%3 == 0:
        return True
    
    return find3(i//10)

for i in range(1,n+1):
    if i % 3 == 0:
        print(0,end=' ')
        continue
    if find3(i):
        print(0,end=' ')
        continue
    print(i, end = ' ')