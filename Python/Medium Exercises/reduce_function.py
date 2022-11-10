from fractions import Fraction
from functools import reduce

def product(fracs):
    res = reduce(lambda x,y: x*y, fracs)
    return res.numerator, res.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    # print(fracs)
    result = product(fracs)
    print(*result)