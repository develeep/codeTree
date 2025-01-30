a,b = map(int,input().split())

dic = {}
result = 0

while a > 1:
    n = a%b
    if n in dic.keys():
        dic[n] += 1
    else:
        dic[n] = 1
    a //= b

for i in dic.values():
    result += i ** 2

print(result)