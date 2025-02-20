n = int(input())
sequence = list(map(int, input().split()))

# Write your code here
arr = [[sequence[i],i,0] for i in range(len(sequence))]
sorted_arr = sorted(arr, key= lambda x: x[0])
for i in range(len(sorted_arr)):
    old_i = sorted_arr[i][1]
    arr[old_i][2] = i
for _,_,i in arr:
    print(i+1,end=' ')