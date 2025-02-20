n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!

arr = []

for s in str:
    for i in range(len(t)):
        if s[i] != t[i]:
            break
    else:
        arr.append(s)

arr.sort()
print(arr[k-1])