input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Write your code here!
for ques in queries:
    if ques == 1:
        input_str = input_str[1:] + input_str[0]
    elif ques == 2:
        input_str = input_str[-1] + input_str[:-1]
    elif ques == 3:
        input_str = input_str[::-1]
    print(input_str)
