from collections import defaultdict

n, m = map(int,input().split())
A = []
B = []

for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())

d = defaultdict(list)
for x in B:
    if x in A:   
        for i in range(len(A)):
            if x == A[i]:
                d[x].append(i+1)
    else:
        d[x].append(-1)
# print(d.values())
for x in d.values():
    print(*x, sep = ' ')