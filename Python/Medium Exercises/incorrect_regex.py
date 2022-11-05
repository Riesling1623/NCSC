# RegEx Module
import re

for _ in range(int(input())):
    try:
        re.compile(input()) #the attribute of re
        print('True')
    except re.error:
        print('False')