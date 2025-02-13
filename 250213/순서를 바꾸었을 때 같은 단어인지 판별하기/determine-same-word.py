word1 = input()
word2 = input()

# Write your code here!
sort_word1 = sorted(word1)
sort_word2 = sorted(word2)

if sort_word1 == sort_word2:
    print('Yes')
else:
    print('No')