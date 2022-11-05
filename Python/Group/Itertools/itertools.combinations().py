# This tool returns the r length subsequences of elements from the input iterable.

# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the 
# combination tuples will be produced in sorted order.

# combinations
from itertools import combinations
inp = list(map(str,input().split()))
s = inp[0]
lst_s = sorted(list(s))
k = int(inp[1])
out_lst = []

for i in range(1,k+1):
    lst = combinations(lst_s,i)
    out_lst += lst

# print(out_lst)
for x in out_lst:
    print(''.join(x))