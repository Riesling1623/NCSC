# You are given the firstname and lastname of a person on two different lines. Your task is to read them 
# and print

def print_full_name(first, last):
    print('Hello ' + first + ' ' + last + '! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name,last_name) 