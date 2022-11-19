import re
regex_pattern = r"^(?=(?:[a-z0-9]*[A-Z]){2,})(?=(?:[a-zA-Z]*[0-9]){3,})(?:([a-zA-Z0-9])(?!.*\1)){10}$"

for _ in range(int(input())):
    UID = input()
    if re.match(regex_pattern, UID):
        print("Valid")
    else:
        print("Invalid")