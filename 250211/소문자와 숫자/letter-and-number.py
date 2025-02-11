s  = input()
result = [x for x in s if x.isalpha() or x.isdigit()]
print(*[a.lower() if a.isalpha() else a for a in result ], sep='')