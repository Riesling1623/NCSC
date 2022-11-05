def init(k, n):
    table = []
    for _ in range(k+1):
        table.append([])
        for _ in range(n+1):
            table[len(table)-1].append(-1)
    return table

def C(k, n):
    global table
    if (k==0) or (k==n):
        table[k][n] = 1
    else:
        if table[k][n] < 0:
            table[k][n] = (C(k-1, n-1) + C(k, n-1)) % (1000000007)
    return table[k][n]

k, n = map(int, input().split())
table = init(k,n)
# print(table)
print(C(k,n))