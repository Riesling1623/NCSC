from collections import Counter
'''
Counter is a container that stores elements as dictionary keys, and their counts
are stored in dictionary values
'''

if __name__ == '__main__':
    s = input()
    l = []
    for alpha in s: #list of all character in string
        l.append(alpha)
    l.sort()
    # print(l)
    freq = (Counter(l))
    # print(freq)
    top_3 = freq.most_common(3) # most_common in Counter
    [print(alpha,count) for alpha ,count in top_3]