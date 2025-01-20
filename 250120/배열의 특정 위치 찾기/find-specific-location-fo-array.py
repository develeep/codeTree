arr = list(map(int,input().split()))

hap = sum(arr[1::2])
avr = sum(arr[2::3]) / len(arr[2::3])

print(hap,f'{avr:.1f}')