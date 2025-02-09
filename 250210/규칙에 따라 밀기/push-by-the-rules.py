s = input()
quest = input()

for q in quest:
    if q == 'L':
        s = s[1:] + s[0]
    elif q == 'R':
        s = s[-1] + s[:-1]
print(s)