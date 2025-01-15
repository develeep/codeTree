n =  int(input())
nums = []

for i in range(1,n):
    if (n%i == 0):
        nums.append(i)

print('P' if sum(nums) == n else 'N')