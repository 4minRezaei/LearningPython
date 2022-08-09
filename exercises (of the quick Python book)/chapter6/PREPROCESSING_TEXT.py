# 6.9 page: 88
'''
In this lab,
the task is to read the first part of the first chapter
of Moby Dick (found in the book's source code),
make sure that everything is one case, remove all punctuation,
and write the words one per line to a second file.
'''

import string
punc = string.punctuation
all_words = list()

with open('moby_01.txt', 'r') as infile:
    for line in infile:
        line = line.lower()
        for letter in line:
            if letter in punc:
                line = line.replace(letter, '')
        all_words.extend(line.split())

with open('moby_01_clean.txt', 'w') as outfile:
    outfile.write('\n'.join(all_words))
