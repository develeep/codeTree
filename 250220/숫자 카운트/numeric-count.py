n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)
cnt = 0
# Write your code here!
for A in range(111,1000):
    a1 = (A//100) % 10
    a2 = (A//10) % 10
    a3 = (A//1) % 10
    if a1 == a2 == a3:
        continue
    if a1 == 0 or a2 == 0 or a3 == 0:
        continue

    flag = 1
    for i in range(n):
        b1 = (a[i]//100) % 10
        b2 = (a[i]//10) % 10
        b3 = (a[i]//1) % 10


        if b[i] != (b1 == a1) + (b2 == a2) + (b3 == a3):
            flag = 0
            break

        same_stack = 6 - len(set([a1,a2,a3,b1,b2,b3]))
        if same_stack - b[i] != c[i]:
            flag = 0
            break

    if flag:
        cnt += 1

print(cnt)