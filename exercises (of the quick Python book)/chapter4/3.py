Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input('what is your name?\n')
what is your name?
Amin
name
'Amin'
age = input('how old are you, {fname}?\n'.format(fname = name))
how old are you, Amin?
24
age
'24'
name
'Amin'
type(age)
<class 'str'>
age = int(input('how old are you, {fname}?\n'.format(fname = name)))
how old are you, Amin?
24
type(age)
<class 'int'>
input('how weight are you, {fname}?\n'.format(fname = name))
how weight are you, Amin?
70.5
'70.5'
weight = float(input('how weight are you, {fname}?\n'.format(fname = name)))
how weight are you, Amin?
70.5
type(name)
<class 'str'>
type(age)
<class 'int'>
type(weight)
<class 'float'>
name
'Amin'
age
24
weight
70.5
#What happens if you deliberately enter the wrong type of value?
age = int(input('age?'))
age?24.5
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    age = int(input('age?'))
ValueError: invalid literal for int() with base 10: '24.5'
