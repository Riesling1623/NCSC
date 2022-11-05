'''
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
'''

N = int(input()) # the total number of country stamps
collection = set()
for _ in range(N):
    collection.add(input())
print(len(collection))