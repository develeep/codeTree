arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr = [arr1,arr2]

avr1 = sum(arr[0]) / 4
avr2 = sum(arr[1]) / 4

print(f'{avr1:.1f}',end=" ")
print(f'{avr2:.1f}')

for i in range(4):
    avr = sum([arr[0][i],arr[1][i]]) / 2
    print(f'{avr:.1f}',end= " ")

print()
hap = 0
for i in range(2):
    for j in range(4):
        hap+= arr[i][j]
avr =  hap/ 8
print(f'{avr:.1f}')