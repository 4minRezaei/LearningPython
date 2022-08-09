"""
Which of the following will not be converted to numbers, and why?
int('a1')
int('12G', 16)
float("12345678901234567890")
int("12*2")
"""

'''int('a1')'''
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     int('a1')
# ValueError: invalid literal for int() with base 10: 'a1'


'''int('12G', 16)'''
# Traceback (most recent call last):
#   File "<pyshell#4>", line 1, in <module>
#     int('12G', 16)
# ValueError: invalid literal for int() with base 16: '12G'


'''int("12*2")'''
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     int("12*2")
# ValueError: invalid literal for int() with base 10: '12*2'


float("12345678901234567890")
# output: 1.2345678901234567e+19
