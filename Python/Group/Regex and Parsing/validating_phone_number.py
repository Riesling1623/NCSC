import re
regex_pattern = r"^[789][0-9]{9}$"

for _ in range(int(input())):
    s = input()
    check = re.match(regex_pattern, s)
    if check:
        print("YES")
    else:
        print("NO")