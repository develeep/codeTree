n, m = map(int, input().split())
dic = set()
a = list(map(int, input().split()))
# Please write your code here.

for i in range(1,n+1):
    dic.add(i)

def f(idx):
    if len(dic) == 0:
        return -1
    arr = sorted(dic)
    down = 0
    top = len(arr)-1

    while 1:
        mid = (top + down) //2

        if down == mid:
            if arr[mid] <= idx:
                dic.remove(arr[mid])
                return 1
            else:
                return -1

        if arr[mid] <= idx:
            down = mid
        
        if arr[mid] > idx:
            top = mid -1
        
        

cnt = 0
for user in a:
    c =  f(user)
    if c == -1:
        break
    cnt += c

print(cnt)

