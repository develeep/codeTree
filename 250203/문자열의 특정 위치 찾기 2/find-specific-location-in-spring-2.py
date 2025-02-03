n = input()

arr = ['apple','banana','grape','blueberry','orange']
result = list(filter(lambda x: n in x[2:4],arr))
result.append(str(len(result)))

print('\n'.join(result))
