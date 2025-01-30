n = int(input())
nums = list(map(int, input().split()))
max_num = -1
# Write your code here!
for i in nums:
    if i > max_num and nums.count(i) == 1:
        max_num = i
    
print(max_num)