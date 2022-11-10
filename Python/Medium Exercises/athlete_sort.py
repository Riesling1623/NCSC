n, m = map(int,input().split())
athletes = []
for _ in range(n):
    athletes.append(list(map(int,input().split())))
k = int(input())
athletes.sort(key = lambda x: x[k])

# print(athletes)
for x in athletes:
    print(*x, sep=' ')