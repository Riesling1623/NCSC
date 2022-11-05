if __name__ == '__main__':
    s = input()
    
    # alphanumeric
    for i in range(len(s)):
        if s[i].isalnum() == True:
            print(True)
            break
        elif i == len(s) - 1 and s[i].isalnum() == False:
            print(False)

    # alphabetical
    for i in range(len(s)):
        if s[i].isalpha() == True:
            print(True)
            break
        elif i == len(s) - 1 and s[i].isalpha() == False:
            print(False)

    # digit
    for i in range(len(s)):
        if s[i].isdigit() == True:
            print(True)
            break
        elif i == len(s) - 1 and s[i].isdigit() == False:
            print(False)

    # lower
    for i in range(len(s)):
        if s[i].islower() == True:
            print(True)
            break
        elif i == len(s) - 1 and s[i].islower() == False:
            print(False)

    # upper
    for i in range(len(s)):
        if s[i].isupper() == True:
            print(True)
            break
        elif i == len(s) - 1 and s[i].isupper() == False:
            print(False)