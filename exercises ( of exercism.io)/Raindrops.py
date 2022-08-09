def convert(number):
    number = int(number)
    dict = {3:'Pling', 5:'Plang', 7:'Plong'}
    ls = [dict[i] for i in dict.keys() if number % i == 0]
    if len(ls) > 0:
        return ''.join(ls)
    else:
        return str(number)