arr = list(map(int,input().split()))
old_max = 1000
old_min = 0


for i in arr:
    if i > 500:
        if old_max-500 > i - 500:
            old_max = i
    else:
        if 500 - old_min > 500 - i:
            old_min = i
    
print(old_min,old_max)