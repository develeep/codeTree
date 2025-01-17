n = int(input())
arr = list(map(float,input().split()))

avr = sum(arr) / len(arr)
print(f'{avr:.1f}')
print('Perfect' if avr >= 4.0 else 'Good' if avr >= 3.0 else 'Poor')

