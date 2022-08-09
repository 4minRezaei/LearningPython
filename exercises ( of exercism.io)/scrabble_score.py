group_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
group_2 = ['D', 'G']
group_3 = ['B', 'C', 'M', 'P']
group_4 = ['F', 'H', 'V', 'W', 'Y']
group_5 = ['K']
group_6 = ['J', 'X']
group_7 = ['Q', 'Z']

dic = {
    1: group_1,
    2: group_2,
    3: group_3,
    4: group_4,
    5: group_5,
    8: group_6,
    10: group_7,
    }

def value_key(value, dictionary):
    for key, val in dictionary.items():
        if val == value:
            return key

def score(word):
    score = 0
    word = word.upper()
    for letter in word:
        for value in dic.values():
            if letter in value:
                score += (value_key(value=value, dictionary=dic))
    return score