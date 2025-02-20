str = input()

# Write your code here!
def check_str(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True

    
print('Yes' if check_str(str) else 'No')