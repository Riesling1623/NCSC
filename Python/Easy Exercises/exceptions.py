T = int(input()) # the number of test cases
for _ in range(T):
    a, b = map(str, input().split())
    try:
        print(int(int(a) // int(b)))
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)  