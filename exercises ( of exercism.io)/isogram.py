def is_isogram(string):
    string = string.lower()
    letters = dict()
    isogram = True
    
    for i in range(len(string)):
        if string[i] == ' ' or string[i] == '-':
            pass
        elif string[i] not in letters:
            letters[string[i]] = 1
        else:
            letters[string[i]] += 1

    for i in letters.values():
        if i > 1:
            isogram = False
            return isogram
    return isogram