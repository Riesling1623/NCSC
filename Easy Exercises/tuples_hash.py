# Use Pypy3 instead of Python3

# Given an integer, n, and n space-separated integers as input, create a tuple, n, of those n integers. 
# Then compute and print the result of hash(t).

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    print(hash(tuple(integer_list)))