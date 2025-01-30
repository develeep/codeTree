idx1, idx2 = map(int,input().split())
n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))
result = 'No'

for i in range(idx1-idx2):
    if result == 'Yes':
        break
    if n1[i] == n2[0]:
        for j in range(idx2):
            if n1[i+j] != n2[j]:
                result = 'No'
                break
            result = 'Yes'

print(result)