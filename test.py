s = input()
characters = {}

for x in s:
    if x not in characters:
        characters[x] = 1
    else:
        characters[x] += 1

# print(list(characters.items()))
# print(characters.values())

lst_characters = sorted(list(characters.items()))
lst_characters_rev_value = sorted([ (v,k) for k,v in lst_characters ])
lst_characters = [ (k,v) for v,k in lst_characters_rev_value ]
print(lst_characters)