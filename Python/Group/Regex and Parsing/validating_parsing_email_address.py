import email.utils
import re
regex_pattern = r"^<[a-z][a-z0-9-._]+@[a-z]+\.[a-z]{1,3}>$"

n = int(input()) # the number of email address
for i in range(n):
    inp = input()
    name, emailAddress = map(str, inp.split())
    check = re.match(regex_pattern, emailAddress, re.I)
    tup = (name, emailAddress)
    if check:
        print(email.utils.formataddr((name, emailAddress)))