n = int(input())
code = ord("A")
z_code = ord("Z")

for i in range(n):
    for j in range(i+1):
        print(chr(code),end="")
        if code == z_code:
            code = ord('A')
            continue
        code += 1
    print()