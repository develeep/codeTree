str1,str2 = input().split()
if len(str1) < len(str2):
    print(str2, len(str2))
elif len(str1) == len(str2):
    print('same')
else:
    print(str1, len(str1))

    