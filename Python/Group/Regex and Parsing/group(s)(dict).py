import re

s = input()
# s = '..12345678910111213141516171820212223'
regex_pattern = r'([a-zA-Z0-9])\1'
'''
\num: find the repetitive character same as group num
'''
m = re.search(regex_pattern, s) # use search to find
if m: # if m be found ==> True
    print(m.group()[0]) # return the first solution that satified
else:
    print(-1)