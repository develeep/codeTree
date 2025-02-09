s, q = input().split()
arr = [*s]
for _ in range(int(q)):
    n,a,b = input().split()

    if n == '1':
        arr[int(a)-1], arr[int(b)-1] = arr[int(b)-1], arr[int(a)-1] 

    elif n == '2':
        for i in range(len(arr)):
            if arr[i] == a:
                arr[i] = b
    print(''.join(arr))

