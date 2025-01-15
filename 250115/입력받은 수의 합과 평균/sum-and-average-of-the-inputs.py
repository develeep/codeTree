n = int(input())
nums = []


for _ in range(n):
    nums.append(int(input()))
    
hap = sum(nums)
avr = hap / len(nums)
print(hap,f'{avr:.1f}')