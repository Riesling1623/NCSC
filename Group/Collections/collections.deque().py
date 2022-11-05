# Perform append, pop, popleft and appendleft methods on an empty deque d.


from collections import deque

d = deque()

n = int(input()) # the number of operations
for _ in range(n):
    method = input().split()

    if 'append' in method:
        d.append(int(method[1]))
    elif 'appendleft' in method:
        d.appendleft(int(method[1]))
    elif 'pop' in method:
        d.pop()
    else:
        d.popleft()

print(*d, sep = ' ')