ban = {
    1: 'John',
    2: 'Tom',
    3: 'Paul',
    4: 'Sam',
}

while 1:
    n = int(input())
    if n > 4 or n < 1:
        print('Vacancy')
        break
    print(ban[n])