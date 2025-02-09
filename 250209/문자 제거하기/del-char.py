s = input()
result = [*s]

while len(result) > 1:
    n = int(input())

    if len(result) <= n:
        result.pop()
    else:
        result.pop(n)
    print(''.join(result))