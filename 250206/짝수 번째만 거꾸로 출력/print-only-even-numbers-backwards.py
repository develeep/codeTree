s = input()

print(s[-1 if len(s) % 2 == 0 else -2::-2])