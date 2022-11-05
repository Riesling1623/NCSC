# Consider the following:

# A string, s, of length n.
# An integer, k, where k is a factor of n.
# We can split s into n/k substrings where each subtring t, consists of a contiguous block of k characters 
# in s. Then, use each substring to create string u such that:

# The characters in u are a subsequence of the characters in t.
# Any repeat occurrence of a character is removed from the string such that each character in u occurs 
# exactly once. In other words, if the character at some index j in t occurs at a previous index <j in t, 
# then do not include the character in string u.
# Given s and k, print n/k lines where each line i denotes string .

import textwrap
def merge_the_tools(string, k):
    substrings_t = textwrap.wrap(string,k)
    # print(substrings)
    # substrings_u = []
    for sub_t in substrings_t:
        sub_s = ''
        for x in sub_t:
            if x not in sub_s:
                sub_s += x
        print(sub_s)     

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string,k)