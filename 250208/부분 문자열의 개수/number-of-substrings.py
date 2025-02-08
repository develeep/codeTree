a = input()
b = input()

count= 0

for i in range(1,len(a)):
    if a[i] == b[1] and a[i-1] == b[0]:
        count += 1

print(count)