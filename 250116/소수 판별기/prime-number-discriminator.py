n = int(input())
result = 'P'

for i in range(2,n):
    if n % i == 0:
        result = 'C'
        break

print(result)