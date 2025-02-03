n = int(input())

arr = [input() for _ in range(n)]
hap = sum(len(i) for i in arr)
a = len([i for i in arr if i[0] == 'a'])
print(hap, a)