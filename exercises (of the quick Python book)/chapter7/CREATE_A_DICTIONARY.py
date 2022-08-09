'''
Write the code to ask the user for three
names and three ages. After the names and ages are entered, ask the user for
one of the names, and print the correct age. 
'''

name_age = dict()
for i in range(3):
    name = input('enter the name: \n')
    age = input('enter the age number: \n')
    name_age[name] = int(age)

while True:
    person = input('who\'s age do you wnat to know? \n' )
    print(person + ' is {0} years old.\n'.format(name_age[person]))
