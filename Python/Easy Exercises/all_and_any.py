def is_palindrome(num):
    num = str(num)
    rev_num = num[::-1]
    if num == rev_num:
        return True
    else:
        return False

n = int(input())
lst = list(map(int,input().split()))

# print(all(x > 0 for x in lst))
if all(x > 0 for x in lst):
    if any(is_palindrome(x) for x in lst):
        print(True)
    else:
        print(False)
else:
    print(False)