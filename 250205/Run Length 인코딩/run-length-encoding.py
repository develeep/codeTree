A = input()

# Write your code here!
arr = list(A)
count = 1
result = [[arr[0],1]]

for idx in range(1,len(arr)):
    if arr[idx] != result[-1][0]:
        result.append([arr[idx],1])

    if arr[idx] == arr[idx-1]:
        result[-1][1] += 1
    



result_str = ''
for r in result:
    result_str += r[0] + str(r[1])

print(len(result_str))
print(result_str)