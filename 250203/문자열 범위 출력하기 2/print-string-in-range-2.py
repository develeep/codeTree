str1 = input()
n = int(input())
if n > len(str1):
    print(str1[::-1])
else:  
    print(str1[:-n-1:-1])