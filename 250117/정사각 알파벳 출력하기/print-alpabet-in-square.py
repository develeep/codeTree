n = int(input())
code = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(code),end="")
        code += 1
    print()