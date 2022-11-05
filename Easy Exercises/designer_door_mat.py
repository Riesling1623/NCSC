# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n, m = map(int,input().split())

for i in range((m//2)-1,0,-3):
    print('-'*i + (".|."*int((m-i*2)/3)) + '-'*i)

print('-'*int(((m-7)/2)) + 'WELCOME' + '-'*int(((m-7)/2)))

for i in range(3,(m//2),3):
    print('-'*i + (".|."*int((m-i*2)/3)) + '-'*i)
