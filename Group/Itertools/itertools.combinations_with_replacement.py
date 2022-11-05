# This tool returns r length subsequences of elements from the input iterable allowing individual elements 
# to be repeated more than once.

# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the 
# combination tuples will be produced in sorted order.

from itertools import combinations_with_replacement

inp = list(map(str,input().split()))
s = inp[0]
k = int(inp[1])
lst_s = sorted(list(s))

output_list = list(combinations_with_replacement(lst_s,k))
for x in output_list:
    print(''.join(x))