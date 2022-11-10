def fun(s):
    if ("@" in s) and ("." in s): # there are at least 1 "@" and "."
        idx_at = s.index("@")
        if idx_at != 0: # if @ is the first character, return False
            idx_dot = s.index(".")
            check = True
            i = 0
            
            # check username
            while s[i] != "@":
                if s[i].isalnum() or s[i] == '-' or s[i] == '_':
                    i += 1
                else:
                    check = False
                    break
            
            # check website name and extension
            if check == True:
                if (s[(idx_at + 1) : (idx_dot)].isalnum() == False):
                    check = False
                else:
                    if s[(idx_dot + 1):].isalpha() == False or len(s[idx_dot + 1:]) > 3:
                        check = False
        else:
            check = False
    else:
        check = False
    return check


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)