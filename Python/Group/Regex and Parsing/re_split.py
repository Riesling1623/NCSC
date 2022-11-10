regex_pattern = r"\W"
'''
\W : Returns a match where the string DOES NOT contain any word characters
(a-Z, 0-9, and underscore)

\W+ : Same as \W but not return ... :))) 
(Try "Words, words, words." to understand)
'''

import re
print("\n".join(re.split(regex_pattern, input())))