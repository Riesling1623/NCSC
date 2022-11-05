# You are asked to ensure that the first and last names of people begin with a capital letter in their 
# passports.

def solve(s):
    s = s.capitalize()
    lst = list(s)
    for i in range(1,len(lst)):
        if (lst[i].isalpha() == True) and lst[i-1] == ' ':
            lst[i] = lst[i].upper()
    return ''.join(lst)

s = input()
print(solve(s))