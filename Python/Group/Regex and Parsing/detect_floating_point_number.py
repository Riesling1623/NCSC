import re

t = int(input())
for _ in range(t):
    n = input()
    try:
        num = float(n)
        if bool(re.search(r".", n)): # case 2: must have exactly one . symbol
            d = re.search(r".", n)
            idx = d.start() # return index of the . symbol
            if idx != len(n) - 1: # case 3: must contain at least 1 decimal value
                print(True)
            else:
                print(False)
        else:
            print(False)
    except ValueError as e:
        '''
        case 1: can't convert to float (because it has a character which 
        is not digit or have 2 signs)
        '''
        print(False)
    
# -+12.5