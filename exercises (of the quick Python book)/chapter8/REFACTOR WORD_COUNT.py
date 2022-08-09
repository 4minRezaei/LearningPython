# lab 8, page 112
'''
Rewrite the word-count program from section
8.7 to make it shorter. You may want to look at the string and list operations
already discussed, as well as think about different ways to organize the code.
You may also want to make the program smarter so that only alphabetic
strings (not symbols or punctuation) count as words.
'''
import string

infile = open('word_count.txt')
lines = infile.read()
table = dict()

for punc in string.punctuation:
    table[ord(punc)] = ''

lines = lines.translate(table)
lines = lines.split('\n')
line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)
print('File has {0} lines, {1} words, {2} characters'.format
     (line_count, word_count, char_count))
