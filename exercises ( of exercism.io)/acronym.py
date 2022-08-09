import string

def abbreviate(words):
    words = words.upper()
    table = dict()
    acronym = []

    for punc in string.punctuation:
        if punc == '-':
            table[ord(punc)] = ' '
        else:
            table[ord(punc)] = ''
    
    words = words.translate(table)
    words = words.split()
    for word in words:
        acronym.append(word[0])
    return ''.join(acronym)
