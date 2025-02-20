A = input()
cnt = 0

# Write your code here!
def check(new_arr):
    global cnt
    if len(new_arr) == 4:
        cnt += 1
        return
    for i in range(len(A)):
        if len(new_arr) == 2:
            if i + 1 < len(A) and A[i] == A[i+1] == ')':
                check(new_arr+[')',')'])
        else:
            if i + 1 < len(A) and A[i] == A[i+1] == '(':
                check(new_arr+['(','('])

check([])
print(cnt)