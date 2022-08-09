'''
What would be a quick way to change all
punctuation in a string to spaces?
'''

import string
punc = string.punctuation

txt = ''' hello.world.this. is . a . test. '''

for letter in txt:
    if letter in punc:
        txt = txt.replace(letter, ' ')

print(txt)
