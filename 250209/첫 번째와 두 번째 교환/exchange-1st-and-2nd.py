a, b, *c = input()

for i in range(len(c)):
    if c[i] == a:
        c[i] = b
    elif c[i] == b:
        c[i] = a

print(b+a+''.join(c))