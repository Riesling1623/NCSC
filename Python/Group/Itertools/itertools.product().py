# itertools.product()

# This tool computes the cartesian product of input iterables.

# cartesian's product
from itertools import product

A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

AxB = list(product(A,B))

for x in AxB:
    print(x,end = ' ')