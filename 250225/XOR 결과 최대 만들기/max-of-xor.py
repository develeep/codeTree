n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!

def find_max(idx,arr):
    if len(arr) == m:
        global max_result
        result = arr[0]
        for i in range(1,len(arr)):
            result = result ^ arr[i]
        max_result = max(max_result, result)
        return

    for i in range(idx,n):
        find_max(i+ 1, arr+[A[i]])

max_result = float('-inf')
find_max(0,[])

print(max_result)