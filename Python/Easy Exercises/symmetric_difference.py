m = int(input())
set_m = set(map(int,input().split()))
# print(set_m)
n = int(input())
set_n = set(map(int,input().split()))

m_n = set_m.difference(set_n)
n_m = set_n.difference(set_m)
mn = m_n.union(n_m)
res = sorted(mn)

for x in res:
    print(x)