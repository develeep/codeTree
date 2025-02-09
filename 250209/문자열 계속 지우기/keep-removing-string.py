A = input()
B = input()
result = [*A]
flag = True

# Write your code here!
while B in A:
    A = A.replace(B,'')

print(A)
