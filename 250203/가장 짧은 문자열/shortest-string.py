arr = list(map(lambda x : len(x) , [input() for _ in range(3)]))

arr.sort()

print(arr[-1] - arr[0])