# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to 
# uppercase letters and vice versa.



def swap_case(s):
    res = ''
    for x in s:
        if x.isupper():
            res += x.lower()
        else:
            res += x.upper()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)