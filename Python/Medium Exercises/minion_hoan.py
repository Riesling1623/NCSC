def minion_game(s):
    # p = ["Stuart", 'Kevin']
    scores = [0,0]
    vowel = 'AEIOU'
    # record = []
    for i in range(len(s)):
        score = len(s) - i
        if s[i] in vowel:
            scores[1] += score
        else:
            scores[0] += score
    
    if scores[0] > scores[1]:
        print(f'Stuart {scores[0]}')
    elif scores[0] < scores[1]:
        print(f'Kevin {scores[1]}')
    else:
        print('Draw')

given_string = input()
minion_game(given_string)