alpha = input()
a,b = 0,0

for i in range(1,len(alpha)):
    if alpha[i] == 'e' and alpha[i-1] == 'e':
        a += 1
    
    if alpha[i] == 'b' and alpha[i-1] == 'e':
        b += 1
    
print(a,b)