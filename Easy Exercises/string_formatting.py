# Given an integer, n, print the following values for each integer i from 1 to n:

# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary

#Question: rjust? 

def print_formatted(number):
    lens = len(str(bin(number))) - 2
    
    for i in range(1,number + 1):
        a = str(i)
        b = str(oct(i))
        c = str(hex(i)).upper()
        d = str(bin(i))
        print(f'{a.rjust(lens)} {b[2:].rjust(lens)} {c[2:].rjust(lens)} {d[2:].rjust(lens)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)