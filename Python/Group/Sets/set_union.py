n = int(input()) # the number of students who have subscribed to the Eng newspaper
Eng = set(map(int,input().split()))
b = int(input()) # the number of students who have subscribed to the Fra newspaper
Fra = set(map(int,input().split()))

total = Eng.union(Fra)
print(len(total))