import re

s = input()
# s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'

regex_partern = r'(?=[^aeiou]([aeiou]{2,})[^aeiou])'
'''
?= : Asserts that the given subpattern can be matched here, 
WITHOUT CONSUMING characters
{because there is no token before ?= ==> return none 
==> all the character as the condition ==> not consume the character}

^ : EXCEPT

(...): Capture everything enclosed {return}

{num,}: There are num or more occurences

'''

m = re.findall(regex_partern, s, re.I)

if m:
    print(*m, sep = '\n')
else:
    print(-1)