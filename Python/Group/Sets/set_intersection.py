n = int(input())
Eng = set(map(int,input().split()))
b = int(input())
Fra = set(map(int,input().split()))

res = Eng.intersection(Fra)
print(len(res))