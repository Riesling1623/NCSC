# This tool returns successive r length permutations of elements in an iterable.

# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the 
# permutation tuples will be produced in a sorted order.

# permutations
from itertools import permutations

inp = list(map(str,input().split()))
# print(s)
s = inp[0]
k = int(inp[1])

lst_s = sorted(list(s))
lst_perm = list(permutations(lst_s,k))
for x in lst_perm:
    print(''.join(x))