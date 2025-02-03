arr = list(map(lambda x : len(x) , [input() for _ in range(3)]))

print(max(arr) - min(arr))