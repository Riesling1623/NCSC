'''
You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.
'''

n = int(input()) # the number of elements in the set s
s = set(map(int, input().split()))
N = int(input()) # the number of commands
for _ in range(N):
    command = input()
    if 'pop' in command:
        s.pop()
    elif 'remove' in command:
        s.remove(int(command[len(command)-1]))
    else:
        s.discard(int(command[len(command)-1]))
print(sum(s))