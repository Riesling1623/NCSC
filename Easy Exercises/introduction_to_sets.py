def average(array):
    set_arr = set(array)
    res = sum(set_arr) / len(set_arr)
    return '%.3f'%res

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int,input().split()))
#     result = average(arr)
#     print(result)