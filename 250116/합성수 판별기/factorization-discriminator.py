n = int(input())
is_c = 0

for i in range(2,n):
    if n % i == 0:
        is_c = 1
        break

print('C' if is_c else 'N')