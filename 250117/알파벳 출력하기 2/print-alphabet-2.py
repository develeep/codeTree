n = int(input())
code = ord('A')
z_code = ord('Z')

for i in range(n):
    for _ in range(i):
        print(" ",end=" ")
    for _ in range(n-i):
        print(chr(code),end=" ")
        if code == z_code:
            code = ord('A')
            continue
        code += 1
    print()