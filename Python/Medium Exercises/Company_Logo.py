s = input()
character = {}
resList = []

for x in s: # character in the string and the occurence
    if x not in character:
        character[x] = 0
    else:
        character[x] += 1

lstKey = sorted(list(character.keys())) # sort Key in ascending order

lstValue = list(character.values())
lstValue.sort(reverse = True) # sort value in descending order

index_lstValue = 0
while index_lstValue < 3: # 3 value in the result
    for c in lstKey:
        if character[c] == lstValue[index_lstValue] and c not in resList:
            resList.append(c)
            break
    index_lstValue += 1

for x in resList:
    print(x, character[x])
