n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dict = {}

for i in range(n):
    a = arr[i]
    if a in dict:
        continue
    
    dict[a] = i+1

res = sorted(dict.items())
for n,i in res:
    print(n,i)