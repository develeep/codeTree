word1 = input()
word2 = input()

# Write your code here!
count_arr = [0] * 128

for w in word1:
    count_arr[ord(w)] += 1

for w in word2:
    count_arr[ord(w)] -= 1

for x in count_arr:
    if x != 0:
        print('No')
        break
else: 
    print('Yes')