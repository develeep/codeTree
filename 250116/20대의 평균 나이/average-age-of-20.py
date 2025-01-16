ages = []
while 1:
    age = int(input())
    if 20 > age or 30 <= age:
        break
    ages.append(age)

avr = sum(ages) / len(ages)

print(f'{avr:.2f}')