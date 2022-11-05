# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
# Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

# For a better understanding of the problem, check the explanation.

from itertools import groupby

s = input()

keys = [k for k,g in groupby(s)]
# print(keys)

len_each_group = [len(list(g)) for k, g in groupby(s)]
# print(len_each_group)

output_list = [(len_each_group[i], int(keys[i])) for i in range(len(keys))]
for x in output_list:
    print(x, end = ' ')