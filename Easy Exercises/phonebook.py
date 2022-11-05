n = int(input())
phonebook = {}

for _ in range(n):
    entry = list(map(str,input().split()))
    phonebook[entry[0]] = int(entry[1])
# print(phonebook)
# query = input()
# print(query in phonebook)

# query = ' '
# while query != '':
#     query = input()
#     if query in phonebook:
#         print(query + '=' + str(phonebook[query]))
#     elif query == '':
#         break
#     else:
#         print('Not found')

while True:
    try:
        query = input()
        if query in phonebook:
            print(query + '=' + str(phonebook[query]))
        else:
            print('Not found')
    except EOFError: # this will break when no input
        break