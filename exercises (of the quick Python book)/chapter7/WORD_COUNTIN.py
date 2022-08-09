#lab7 page 98
'''
In the previous lab, you took the text of the first chapter of Moby Dick, normalized the case, removed punctuation, and wrote the
separated words to a file. In this lab, you read that file, use a dictionary to
count the number of times each word occurs, and then report the most common and least common words.
'''


infile = open('moby_01_clean.txt')
all_words = dict()
most_common = 1
most_common_word = ''
least_common = 1
least_common_word = ''

for line in infile:
    for word in line.split():
        all_words[word] = all_words.get(word, 0)+1

for word in all_words:
    if all_words[word] > most_common:
        most_common_word = word
        most_common = all_words[word]

    if all_words[word] <= least_common:
        least_common_word = word
        least_common = all_words[word]


print('most common word is: {0}, wich occurs {1} times.'.format(most_common_word, most_common))
print('least common word is: {0}, wich occurs {1} times.'.format(least_common_word, least_common))
