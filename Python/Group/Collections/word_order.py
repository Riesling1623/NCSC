from collections import OrderedDict
wordList = OrderedDict()

n = int(input())
for _ in range(n):
    word = input()
    
    if word not in wordList:
        wordList[word] = 1
    else:
        wordList[word] += 1

print(len(wordList))
print(*wordList.values(), sep = ' ')