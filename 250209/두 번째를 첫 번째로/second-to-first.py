string = input()
result = ''
for s in string:
    if s == string[1]:
        result += string[0]
    else:
        result += s

print(result)