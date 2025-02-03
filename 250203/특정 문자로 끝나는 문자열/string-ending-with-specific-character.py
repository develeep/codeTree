arr = [input() for _ in range(10)]
n = input()

result = [word for word in arr if word.endswith(n)]
if len(result) == 0:
    print('None')
else:
    print(*result,sep="\n")