# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    N = input()
    if re.match('^[+-]{0,1}\d*\.\d+$',N):
        print('True')
    else:
        print('False')