#? from functools import reduction
#* ImportError: cannot import name 'reduction' from 'functools'

#? from maths import add, subtract, multiply, divide, square, cube, power, modulo
# ?from math import 
# #* wrong import *
import math
# * ModuleNotFoundError: No module named 'maths'
def formatted_country():
    countries=[
        [
            ("Finland", "Helsinki"),
            ("Sweden", "Stockholm"),
            ("Norway", "Oslo")
        ]
    ]
    list=[
        [country,country[0:3],capital]
        for outer in countries
        # for inner in outer
        for (country,capital) in outer
            ]
    return list
# print(formatted_country())
#* TypeError: 'str' object is not callable in case of multiple for loops in list comprehension

# print(food_stuff_li[0],food_stuff_li[1],food_stuff_li[-1],food_stuff_li[-2])
# Output:
# Fish Kebab Hari matar Chana
# del food_stuff_tp
# print(food_stuff_tp)
# Output:
#* NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_li'?
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
try:
    pass
    # print(nordic_countries.index('India'))
    # print('India' in nordic_countries)
# Works for tuple as well as list, in and not in
except ValueError:
    pass
    #? print("Doesn't exists")
#* ValueError: tuple.index(x): x not in tuple
#* IndentationError: expected an indented block after 'except' statement on line 32
#? print 'hello world'
#* SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# ?print(age)

#* NameError: name 'age' is not defined

# print(nordic_countries[7])
#* IndexError: tuple index out of range

# ?print(math.pi)
#* NameError: name 'math' is not defined
#* ModuleError: No module named 'math' wrong import

#? print(math.PI)
#* AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

#? users = {'name':'Asab', 'age':250, 'country':'Finland'}
#? print(users['names'])
#* KeyError: 'names'

#?print(4+3+'')
#* TypeError: unsupported operand type(s) for +: 'int' and 'str'
a=3
try:
    for i in range(9):
        print(a/i)
except ZeroDivisionError:
     for i in range(9):
        if(i!=0):
            print(a/i)
#* ZeroDivisionError: division by zero
# 3.0
# 1.5
# 1.0
# 0.75
# 0.6
# 0.5
# 0.42857142857142855
# 0.375
# TypeError: __main__.unpacking_country_info() argument after ** must be a mapping, not list
# Expecting a dictionary