n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max_idx = [a.index(max(a))]
while max_idx[-1] > 0:
    max_idx.append(a.index(max(a[:max_idx[-1]])))

for i in max_idx:
    print(i+1,end=" ")