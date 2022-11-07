n = int(input())
Eng = set(map(int,input().split()))
b = int(input())
Fra = set(map(int,input().split()))

res = Eng.difference(Fra)
print(len(res))