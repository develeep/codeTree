n,q = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(q):
    input_arr = list(map(int,input().split()))

    if input_arr[0] == 1:
        print(arr[input_arr[1]-1])
    elif input_arr[0] == 2:
        if input_arr[1] in arr:
            print(arr.index(input_arr[1])+1)
        else:
            print(0)
    else:
        for i in range(input_arr[1]-1,input_arr[2]):
            print(arr[i],end=" ")
        print()

