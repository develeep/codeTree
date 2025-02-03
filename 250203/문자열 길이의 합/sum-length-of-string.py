n = int(input())

arr = [input() for _ in range(n)]
hap = sum(len(i) for i in arr)
a = sum(1 for i in arr if i.startswith('a'))
print(hap, a)