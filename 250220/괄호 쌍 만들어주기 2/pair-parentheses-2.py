A = input()
cnt = 0

# Write your code here!
def check(new_arr,index):
    global cnt
    if len(new_arr) == 4:
        cnt += 1
        return
    for i in range(index,len(A)):
        if len(new_arr) == 2:
            if i + 1 < len(A) and A[i] == A[i+1] == ')':
                check(new_arr+[')',')'],i+1)
        else:
            if i + 1 < len(A)-2 and A[i] == A[i+1] == '(':
                check(new_arr+['(','('],i+1)

check([],0)
print(cnt)