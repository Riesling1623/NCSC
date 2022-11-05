# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as 
# dictionary values.
from collections import Counter

# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of 
# their desired size.

# Your task is to compute how much money Raghu earned.

# x: the number of shoes
x = int(input())
shoe_sizes_list = list(map(int,input().split()))
all_shoes = Counter(shoe_sizes_list)
earning = 0

# n: the number of customers
n = int(input())

for _ in range(n):
    customer = list(map(int,input().split()))
    if customer[0] in all_shoes.keys() and all_shoes[customer[0]] != 0:
        earning += customer[1]
        all_shoes[customer[0]] -= 1

print(earning)