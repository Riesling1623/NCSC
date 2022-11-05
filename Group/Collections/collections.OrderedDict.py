'''
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
'''

from collections import OrderedDict

N = int(input())
list_items = OrderedDict()

for _ in range(N):
    item = input().rsplit(' ', 1)
    if item[0] not in list_items:
        list_items[item[0]] = int(item[1])
    else:
        list_items[item[0]] += int(item[1])

# print(list_items)
for x in list_items.items():
    print(*x, sep=' ')