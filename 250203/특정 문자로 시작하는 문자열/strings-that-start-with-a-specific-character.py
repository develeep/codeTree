n = int(input())
arr = [input() for _ in range(n)]
m = input()

result = [len(i) for i in arr if i.startswith(m)]
print(len(result), f'{sum(result) / len(result):.2f}')