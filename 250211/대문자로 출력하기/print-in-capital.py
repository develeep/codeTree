a = [*input()]
result = filter(lambda x: x.isalpha(),a)
print(*[x.upper() for x in result], sep='')