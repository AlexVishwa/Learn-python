_See older readme: [Click here](./README.old.md) (README.old.md)_

## What is `error`, `exception` and `exception handling` in python. Be concise. (ChatGPT)

Error: An issue in the program's syntax or logic that causes it to fail. Errors can be syntax errors (e.g., SyntaxError) or runtime errors (e.g., NameError, TypeError).

Exception: A type of runtime error that can be caught and handled using try-except blocks. Examples include ValueError, KeyError, and ZeroDivisionError.

*Errors terminate the program if unhandled, while exceptions allow for controlled recovery.*

**What is exception handling?**

Exception handling in Python refers to the process of managing and responding to runtime errors (exceptions) to prevent program crashes. It involves using constructs like `try`, `except`, `else`, and `finally` to handle exceptions gracefully.

Example:

```python
try:
    x = 10 / 0  # Potential exception
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handle the exception
else:
    print("No exceptions occurred.")  # Executes if no exceptions
finally:
    print("Execution complete.")  # Always executes
```

This ensures the program continues running even when unexpected issues arise.

# 30 Days of Python

Code generate via autodocs


## File - `30-days-python-asabeneh/day_01/2.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.3.py -->
```py
a = 4
b = 3
print(f"{a} + {b} = {a +b}")  #         4 + 3 = 7
print(f"{a} - {b} = {a - b}")  #        4 - 3 = 1
print(f"{a} * {b} = {a * b}")  #        4 * 3 = 12
print(f"{a} / {b} = {a / b:.2f}")  #    4 / 3 = 1.33
print(f"{a} % {b} = {a % b}")  #        4 % 3 = 1
print(f"{a} // {b} = {a // b}")  #      4 // 3 = 1
print(f"{a} ** {b} = {a ** b}")  #      4 ** 3 = 64
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_01/2.4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.4.py -->
```py
simple = "Python"
a, b, c, d, e, f = simple  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.5.py -->
```py
language = "Python"
pto = language[0:6:2]  #
print(pto)  # "Pto"
print(type(pto) == str)  # True
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/3.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.1.py -->
```py
# Print weight in pounds, kg.
print("This is weight calculate machine...")


def toKg(pounds):
    return pounds / 2.2046


def toPounds(kg):
    return kg * 2.2046


def userInput():
    print("Q. Please choose pounds or kgs (p/k)...")
    choice = input("")
    if choice == "p":
        print("You choose pounds!!")
        pounds = int(input())
        print(toKg(pounds))

    elif choice == "k":
        print("You choose kgs")
        kg = int(input())
        print(toPounds(kg))
    else:
        print("You choose wrong, choose again!")
        userInput()


userInput()
```
<!-- MARKDOWN-AUTO-DOCS:END -->
## File - `30-days-python-asabeneh/day_02/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/2.py -->
```py
first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/2.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/3.py -->
```py
# int to float
num_int = 10
print("num_int", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = "10.6"
num_float = float(num_str)
print("num_float", float(num_str))  # 10.6
num_int = int(num_float)
print("num_int", int(num_int))  # 10

# str to list
first_name = "Asabeneh"
print(first_name)  # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/3.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex01.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex01.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex01.py -->
```py
# num_one to the power of num_two
num_1 = 2
num_2 = 3

final_value = num_1**num_2
print(final_value)  # 8


# Find floor division of num_1 by num_2 and assign the value to a variable floor_division
final_value2 = num_2 // num_1
print(final_value2)  # 1
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex01.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex02.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex02.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex02.py -->
```py
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

radius = input("Enter radius of circle: ")  # assuming input as 3
r = int(radius)
area_of_circle = 3.14 * r**2
print(area_of_circle)  # 28.26


circum_of_circle = 2 * 3.14 * r
print(circum_of_circle)  # 18.84
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex02.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex03.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex03.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex03.py -->
```py
help("keywords")
# Output
"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not    
"""
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex03.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/1.py -->
```py
s='30 days'
t=' of'
u=' python'
r=s+t+u
print(r)

company="Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print("Title"+company.title())

print("Swapcase :"+company.swapcase())

print(company[0:6])

# print(company.index('coding'))

print(company.replace('Coding', 'fun'))

print(company.split(' '))

companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(','))

print(companies[0])

print(len(company.split(' ')))
#str=company.split(' ')

#print(str[1])

print(company[10])

quote= 'Python For Everyone'

str2= company.split(' ')

for str in str2:
    print(str[0])


quote= 'Python For Everyone'

print(quote.find('P'))

stmt='Coding For All'

print(stmt.find('F'))

print(stmt.rfind('o'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

sentence='You cannot end a sentence with because because because is a conjunction'
str3='because because because'
occ=sentence.index('because')
length_of_substr=len(str3)
print(occ)
print(length_of_substr)
print(sentence[occ:(occ+length_of_substr)])

str='Coding For All'
print(str.startswith('Coding'))
print(str.endswith('coding'))

str='   Coding For All      '
print(f'{str} after stripping {str}')
# print(str.rtrim)

str='I am enjoying this challenge.\nI just wonder what is next.'
print(str)

fields=['Name','Age','Class','Designation']
values=['Alex','25','6','Indep']
print(f'{fields[0]}\t{fields[1]}\t{fields[2]}\t{fields[3]}')
print(f'{values[0]}\t{values[1]}\t{values[2]}\t{values[3]}')

radius=10
Area= 3.14*(radius**2)
print(f'Radius = {radius}')
print(f'Area = 3.14 * 2 ** {radius}')
print(f'The area of a circle with radius {radius} is {Area} meters square.')

a=8
b=6
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_05/1.py -->
```py
list1= []
list2=['Apple','Mango','Strawberry','Banana', 'Kela', 'Orange']
length_of_list=len(list2)
print(length_of_list)

print(list2[0])
print(list2[-1])

if(length_of_list%2 == 0):
    len1=length_of_list/2
    print(list2[int(len1)])
else:
    len2=length_of_list+1/2
    print(list2[int(len2)])

mixed_data_types=['Alex',31,'5\'8"', 'Unmarried']
print(mixed_data_types)

it_companies=['Facebook','Apple','Google','Microsoft','IBM','Oracle','Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])

print(it_companies[-1])
length_of_list=len(it_companies)
if(length_of_list%2 == 0):
    len1=length_of_list/2
    print(it_companies[int(len1)])
else:
    len2=(length_of_list+1)/2
    print(it_companies[int(len2)])


it_companies.append('VIOM')
print(it_companies)

length_of_list=len(it_companies)
if(length_of_list%2 == 0):
    len1=length_of_list/2
    it_companies[int(len1)]='New'
else:
    len2=(length_of_list+1)/2
    it_companies[int(len2)]='New'

print(it_companies)
list2=['#;']
it_companies.extend(list2)
print(it_companies)
if(it_companies[2]=='IBM'):
    print('IBM')
else:
    print(it_companies[2].upper())

# for company in length_of_list:
    # i=0
    # it_companies[i]=company+'#;'
    # i=i+1

# for company in it_companies:
    # print(company)

# if(it_companies.find('infosys')):
    # print(it_companies.find('infosys'))
# else:
    # print('Not found')
# print(sorted(it_companies))
it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])

print(it_companies[-1:-2])

if(int(len(it_companies) % 2) == 0 ):
    l=int(len(it_companies))
    print(it_companies[l/2])
else:
    l=int(len(it_companies)/2)
    print(it_companies[l] ,it_companies[l+1])

it_companies.pop(0)


if(int(len(it_companies) % 2) == 0 ):
    l=int(len(it_companies))
    # print(it_companies[l/2])
    # it_companies.pop(l)
else:
    l=int(len(it_companies)/2)
    # print(it_companies[l] ,it_companies[l+1])
    # it_companies.pop(l)
    # it_companies.pop(l+1)

it_companies.pop(-1)

it_companies.clear()

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack= front_end+back_end
full_stack.insert(9,'Python')
full_stack.insert(10,'Sql')
print(full_stack)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_05/level2.py -->
```py
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def bsort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if(arr[i]>arr[i+1]):
                temp=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
    return arr

print(bsort(ages))
# Output:
# [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

min=ages[0]
max=ages[-1]
print(f"The minimum age is {min}")
print(f'The maximum age is {max}')
# Output:
# The minimum age is 19
# The maximum age is 26
ages.append(min)
ages.append(max)
print(ages)
# Output:
# [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
bsort(ages)
if((len(ages)-1)%2==0):
    median=ages[int((len(ages)-1)/2)]
else:
    median=int((ages[int((len(ages)-1)/2)]+ages[int((len(ages)-1)/2)+1])/2)
print(median)
# Output
# 24
sum=0
for i in range(len(ages)-1):
    sum=sum+ages[i]
avg= int(sum/(len(ages)-1))

print(f'the average age is {avg}')
# # Output:
# the average age is 22
ran=ages[-1]-ages[0]
print(f'The range of age is {ran}')
# The range of age is 7
a=abs(min-avg)
b=abs(avg-max)
if(a>b):
    print("Minimum is much lesser than Average")
else:
    print("Maximum is larger than Average")
    # Output:
    # Maximum is larger than Average

# Questions
    # Find the middle country(ies) in the countries list
    # Divide the countries list into two equal lists if it is even if not one more country for the first half.
    # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_06/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_06/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_06/level1.py -->
```py
tuple1=tuple()
tuple1=('Shubham','Mansi','Aastha','Anshita')
bro=('Shubham','Deepak')
sis=('Aastha','Anjali','Mansi')
siblings=bro+sis
print(siblings)
length=len(siblings)
print(f'("My siblings"= {length})')
family_members=list(siblings)
family_members.extend(['Shri Anand Prakash','Shrimati Laxmi'])
family_members=tuple(family_members)
print(f'Family={family_members}')
############Level2###################
family_members=list(family_members)
parents=family_members[5:7]
siblings=family_members[0:5]
print(siblings)
print(parents)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_06/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_06/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_06/level2.py -->
```py
# level2 continued from level1
fruits=tuple()
fruits=('Apple','Guava','Pomegranate','Pineapple','Custard Apple')
veggies=tuple()
veggies=('Baigan','Ghiya','Petha','Chana','Hari matar')
animalprod=tuple()
animalprod=('Fish','Kebab','Rolls')
food_stuff_tp=animalprod+fruits+veggies
print(food_stuff_tp)
# Output:
# ('Fish', 'Kebab', 'Rolls', 'Apple', 'Guava', 'Pomegranate', 'Pineapple', 'Custard Apple', 'Baigan', 'Ghiya', 'Petha', 'Chana', 'Hari matar')
food_stuff_li=list(food_stuff_tp)
length=len(food_stuff_li)-1
print(food_stuff_li[int(length/2)])
#Output:
# Pineapple
print(food_stuff_li[0],food_stuff_li[1],food_stuff_li[-1],food_stuff_li[-2])
# Output:
# Fish Kebab Hari matar Chana
# del food_stuff_tp
# print(food_stuff_tp)
# Output:
# NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_li'?
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
try:
    print('India' in nordic_countries)
# Works for tuple as well as list, in and not in
except:
    print("Doesn't exists")
# ValueError: tuple.index(x): x not in tuple
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level_1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level_1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_07/level_1.py -->
```py
it_companies=['Facebook','Apple','Google','Microsoft','IBM','Oracle','Amazon']

set1= set(it_companies)
length_of_set=len(set1)

set1.add('Twitter')

set2={'Viom','Keymouse','Mouse'}
set3=set1.union(set2)
print(set3)

set1.remove('Twitter')

set1.discard('Codebrew')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level_2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level_2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_07/level_2.py -->
```py
setA={'Cricket','Football','Badminton','Tennis','Golf'}
setB={'Chess','Checkers','Carrom'}

setC=setA.union(setB)
print(setC)

setD=setA.intersection(setB)
print(setD)

setE=setA.difference(setD)
print(setE)

print(setA.isdisjoint(setB))

print(setA.symmetric_difference(setB))
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level3.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_07/level3.py -->
```py
age = [22, 19, 24, 25, 26, 24, 25, 24]
set1=set(age)
# Output: {19, 22, 24, 25, 26}
print(len(set1))
# Output: 5
print('Length of list is more as it has repeated characters {}'.format(len(age)))

sentence="I am a teacher and I love to inspire and teach people."
sentence=sentence.replace('.','')#this helps to remove full stop at the last
listofwords=sentence.split(' ')
print(listofwords)
set2=set(listofwords)
print(set2)
print("Repeated words are {}".format(len(listofwords)-len(set2)))
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_08/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_08/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_08/level1.py -->
```py
dog=dict()
dog={"name":"chunmun","color":"white","weight":"15kg","breed":"pomeranian"}
print(dog)
student={ "first_name":"Rudra", "last_name":"Chowdhary", "gender": "Male", "age": 24, "marital status":"Unmarried", "skills":["React","NodeJs"], "country": "IN", "city": "GZB","address": "XYX"}
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('HTML')

print(student.items())  #Converted dict to a tuple of key value pairs

student.pop('age')
print(student)

del(dog)    #goodbye chunmun
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_09/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_09/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_09/level1.py -->
```py
# age=int(input("Enter your age"))
# if age<18 :
#     print("Wait for missing years")
# else:
#     print("Fit to drive")

my_age=int(input(print('My age \n')))
yours_age=int(input(print('Yours age \n')))
if (yours_age > my_age):
    if(yours_age - my_age == 1):
        print('you are just one year old')
    print(f'you are just{yours_age - my_age} year old')
elif (yours_age==my_age):
    print("we are of same age")
else:
    print('I am older than u')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_10/1.py -->
```py
for a in range(10):
    print(a)
a=0
while(a < 10):
    print(a)
    a=a+1
for a in range(10,0):
    print(a)
a=10
while(a>0):
    print(a)
    a=a-1
# Output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

for i in range(1,8):
    pattern=['#']
    for j in range(1,i):
        pattern.append('#')
    print(f'{pattern}')

#Output:
# ['#']
# ['#', '#']
# ['#', '#', '#']
# ['#', '#', '#', '#']
# ['#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
for i in range(1,8):
    # pattern=tuple()
    for j in range(1,8):
        # pattern.extends(['#'])
        pass
    # print(f'{pattern}')
    pass
#AttributeError: 'tuple' object has no attribute 'extends'
# Needed Output:
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
for i in range(1,11):
    j=i*i
    print(f'{i}\tx\t{i}\t={j}')
# 1       x       1       =1
# 2       x       2       =4
# 3       x       3       =9
# 4       x       4       =16
# 5       x       5       =25
# 6       x       6       =36
# 7       x       7       =49
# 8       x       8       =64
# 9       x       9       =81
# 10      x       10      =100
list1=['Python','Django','Sql','Xuz']
for o in list1:
    print(o)

print('Even numbers')
for i in range(100):
    if(i%2==0):
        print(i)

print('odd numbers')
for i in range(100):
    if(i%2!=0):
        print(i)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_10/level2.py -->
```py
# import '..\day_01\1.py'
sum=0
for i in range(101):
    sum= sum+ i

print(f"The sum of first 100 numbers is{sum}")

sum=0
for i in range(101):
    if(i%2!=0):
        sum=sum+i
print(f"The sum of odd numbers{sum}")
sum=0
for i in range(101):
    if(i%2==0):
        sum=sum+i
print(f"The sum of even numbers {sum}")
#Output:
# The sum of first 100 numbers is5050
# The sum of odd numbers2500  
# The sum of even numbers 2550
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/level3.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_10/level3.py -->
```py
# from ../data/countries import countries
import sys
sys.path.append('../data')
# import countries_data
print(countries)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
sum=0
for country in countries:
    if(country.find('land')!=-1):
        print(country)
        sum=sum+1
print("The matched countries are {}".format(str(sum)))

fruits=['banana', 'orange', 'mango', 'lemon']
# print(1+'2')
fruits2=[]
for i in range(len(fruits)-1,-1,-1):
    fruits2.append(fruits[i])

print(fruits2)
#output:
# ['lemon', 'mango', 'orange', 'banana']
countries_data=[
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
    {
        "name": "Bahrain",
        "capital": "Manama",
        "languages": [
            "Arabic"
        ],
        "population": 1404900,
        "flag": "https://restcountries.eu/data/bhr.svg",
        "currency": "Bahraini dinar"
    },
    {
        "name": "Bangladesh",
        "capital": "Dhaka",
        "languages": [
            "Bengali"
        ],
        "population": 161006790,
        "flag": "https://restcountries.eu/data/bgd.svg",
        "currency": "Bangladeshi taka"
    },
    {
        "name": "Barbados",
        "capital": "Bridgetown",
        "languages": [
            "English"
        ],
        "population": 285000,
        "flag": "https://restcountries.eu/data/brb.svg",
        "currency": "Barbadian dollar"
    },
    {
        "name": "Belarus",
        "capital": "Minsk",
        "languages": [
            "Belarusian",
            "Russian"
        ],
        "population": 9498700,
        "flag": "https://restcountries.eu/data/blr.svg",
        "currency": "New Belarusian ruble"
    },
    {
        "name": "Belgium",
        "capital": "Brussels",
        "languages": [
            "Dutch",
            "French",
            "German"
        ],
        "population": 11319511,
        "flag": "https://restcountries.eu/data/bel.svg",
        "currency": "Euro"
    },
    {
        "name": "Belize",
        "capital": "Belmopan",
        "languages": [
            "English",
            "Spanish"
        ],
        "population": 370300,
        "flag": "https://restcountries.eu/data/blz.svg",
        "currency": "Belize dollar"
    },
    {
        "name": "Benin",
        "capital": "Porto-Novo",
        "languages": [
            "French"
        ],
        "population": 10653654,
        "flag": "https://restcountries.eu/data/ben.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
    {
        "name": "Bolivia (Plurinational State of)",
        "capital": "Sucre",
        "languages": [
            "Spanish",
            "Aymara",
            "Quechua"
        ],
        "population": 10985059,
        "flag": "https://restcountries.eu/data/bol.svg",
        "currency": "Bolivian boliviano"
    },
    {
        "name": "Bonaire, Sint Eustatius and Saba",
        "capital": "Kralendijk",
        "languages": [
            "Dutch"
        ],
        "population": 17408,
        "flag": "https://restcountries.eu/data/bes.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "languages": [
            "Bosnian",
            "Croatian",
            "Serbian"
        ],
        "population": 3531159,
        "flag": "https://restcountries.eu/data/bih.svg",
        "currency": "Bosnia and Herzegovina convertible mark"
    },
    {
        "name": "Botswana",
        "capital": "Gaborone",
        "languages": [
            "English",
            "Tswana"
        ],
        "population": 2141206,
        "flag": "https://restcountries.eu/data/bwa.svg",
        "currency": "Botswana pula"
    },
    {
        "name": "Bouvet Island",
        "capital": "",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/bvt.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Brazil",
        "capital": "Brasília",
        "languages": [
            "Portuguese"
        ],
        "population": 206135893,
        "flag": "https://restcountries.eu/data/bra.svg",
        "currency": "Brazilian real"
    },
    {
        "name": "British Indian Ocean Territory",
        "capital": "Diego Garcia",
        "languages": [
            "English"
        ],
        "population": 3000,
        "flag": "https://restcountries.eu/data/iot.svg",
        "currency": "United States dollar"
    },
    {
        "name": "United States Minor Outlying Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 300,
        "flag": "https://restcountries.eu/data/umi.svg",
        "currency": "United States Dollar"
    },
    {
        "name": "Virgin Islands (British)",
        "capital": "Road Town",
        "languages": [
            "English"
        ],
        "population": 28514,
        "flag": "https://restcountries.eu/data/vgb.svg",
        "currency": "[D]"
    },
    {
        "name": "Virgin Islands (U.S.)",
        "capital": "Charlotte Amalie",
        "languages": [
            "English"
        ],
        "population": 114743,
        "flag": "https://restcountries.eu/data/vir.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Brunei Darussalam",
        "capital": "Bandar Seri Begawan",
        "languages": [
            "Malay"
        ],
        "population": 411900,
        "flag": "https://restcountries.eu/data/brn.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Bulgaria",
        "capital": "Sofia",
        "languages": [
            "Bulgarian"
        ],
        "population": 7153784,
        "flag": "https://restcountries.eu/data/bgr.svg",
        "currency": "Bulgarian lev"
    },
    {
        "name": "Burkina Faso",
        "capital": "Ouagadougou",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 19034397,
        "flag": "https://restcountries.eu/data/bfa.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Burundi",
        "capital": "Bujumbura",
        "languages": [
            "French",
            "Kirundi"
        ],
        "population": 10114505,
        "flag": "https://restcountries.eu/data/bdi.svg",
        "currency": "Burundian franc"
    },
    {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "languages": [
            "Khmer"
        ],
        "population": 15626444,
        "flag": "https://restcountries.eu/data/khm.svg",
        "currency": "Cambodian riel"
    },
    {
        "name": "Cameroon",
        "capital": "Yaoundé",
        "languages": [
            "English",
            "French"
        ],
        "population": 22709892,
        "flag": "https://restcountries.eu/data/cmr.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Canada",
        "capital": "Ottawa",
        "languages": [
            "English",
            "French"
        ],
        "population": 36155487,
        "flag": "https://restcountries.eu/data/can.svg",
        "currency": "Canadian dollar"
    },
    {
        "name": "Cabo Verde",
        "capital": "Praia",
        "languages": [
            "Portuguese"
        ],
        "population": 531239,
        "flag": "https://restcountries.eu/data/cpv.svg",
        "currency": "Cape Verdean escudo"
    },
    {
        "name": "Cayman Islands",
        "capital": "George Town",
        "languages": [
            "English"
        ],
        "population": 58238,
        "flag": "https://restcountries.eu/data/cym.svg",
        "currency": "Cayman Islands dollar"
    },
    {
        "name": "Central African Republic",
        "capital": "Bangui",
        "languages": [
            "French",
            "Sango"
        ],
        "population": 4998000,
        "flag": "https://restcountries.eu/data/caf.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chad",
        "capital": "N'Djamena",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 14497000,
        "flag": "https://restcountries.eu/data/tcd.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chile",
        "capital": "Santiago",
        "languages": [
            "Spanish"
        ],
        "population": 18191900,
        "flag": "https://restcountries.eu/data/chl.svg",
        "currency": "Chilean peso"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": [
            "Chinese"
        ],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "Christmas Island",
        "capital": "Flying Fish Cove",
        "languages": [
            "English"
        ],
        "population": 2072,
        "flag": "https://restcountries.eu/data/cxr.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Cocos (Keeling) Islands",
        "capital": "West Island",
        "languages": [
            "English"
        ],
        "population": 550,
        "flag": "https://restcountries.eu/data/cck.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Colombia",
        "capital": "Bogotá",
        "languages": [
            "Spanish"
        ],
        "population": 48759958,
        "flag": "https://restcountries.eu/data/col.svg",
        "currency": "Colombian peso"
    },
    {
        "name": "Comoros",
        "capital": "Moroni",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 806153,
        "flag": "https://restcountries.eu/data/com.svg",
        "currency": "Comorian franc"
    },
    {
        "name": "Congo",
        "capital": "Brazzaville",
        "languages": [
            "French",
            "Lingala"
        ],
        "population": 4741000,
        "flag": "https://restcountries.eu/data/cog.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Congo (Democratic Republic of the)",
        "capital": "Kinshasa",
        "languages": [
            "French",
            "Lingala",
            "Kongo",
            "Swahili",
            "Luba-Katanga"
        ],
        "population": 85026000,
        "flag": "https://restcountries.eu/data/cod.svg",
        "currency": "Congolese franc"
    },
    {
        "name": "Cook Islands",
        "capital": "Avarua",
        "languages": [
            "English"
        ],
        "population": 18100,
        "flag": "https://restcountries.eu/data/cok.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Costa Rica",
        "capital": "San José",
        "languages": [
            "Spanish"
        ],
        "population": 4890379,
        "flag": "https://restcountries.eu/data/cri.svg",
        "currency": "Costa Rican colón"
    },
    {
        "name": "Croatia",
        "capital": "Zagreb",
        "languages": [
            "Croatian"
        ],
        "population": 4190669,
        "flag": "https://restcountries.eu/data/hrv.svg",
        "currency": "Croatian kuna"
    },
    {
        "name": "Cuba",
        "capital": "Havana",
        "languages": [
            "Spanish"
        ],
        "population": 11239004,
        "flag": "https://restcountries.eu/data/cub.svg",
        "currency": "Cuban convertible peso"
    },
    {
        "name": "Curaçao",
        "capital": "Willemstad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi",
            "English"
        ],
        "population": 154843,
        "flag": "https://restcountries.eu/data/cuw.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Cyprus",
        "capital": "Nicosia",
        "languages": [
            "Greek (modern)",
            "Turkish",
            "Armenian"
        ],
        "population": 847000,
        "flag": "https://restcountries.eu/data/cyp.svg",
        "currency": "Euro"
    },
    {
        "name": "Czech Republic",
        "capital": "Prague",
        "languages": [
            "Czech",
            "Slovak"
        ],
        "population": 10558524,
        "flag": "https://restcountries.eu/data/cze.svg",
        "currency": "Czech koruna"
    },
    {
        "name": "Denmark",
        "capital": "Copenhagen",
        "languages": [
            "Danish"
        ],
        "population": 5717014,
        "flag": "https://restcountries.eu/data/dnk.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Djibouti",
        "capital": "Djibouti",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 900000,
        "flag": "https://restcountries.eu/data/dji.svg",
        "currency": "Djiboutian franc"
    },
    {
        "name": "Dominica",
        "capital": "Roseau",
        "languages": [
            "English"
        ],
        "population": 71293,
        "flag": "https://restcountries.eu/data/dma.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Dominican Republic",
        "capital": "Santo Domingo",
        "languages": [
            "Spanish"
        ],
        "population": 10075045,
        "flag": "https://restcountries.eu/data/dom.svg",
        "currency": "Dominican peso"
    },
    {
        "name": "Ecuador",
        "capital": "Quito",
        "languages": [
            "Spanish"
        ],
        "population": 16545799,
        "flag": "https://restcountries.eu/data/ecu.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "languages": [
            "Arabic"
        ],
        "population": 91290000,
        "flag": "https://restcountries.eu/data/egy.svg",
        "currency": "Egyptian pound"
    },
    {
        "name": "El Salvador",
        "capital": "San Salvador",
        "languages": [
            "Spanish"
        ],
        "population": 6520675,
        "flag": "https://restcountries.eu/data/slv.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Equatorial Guinea",
        "capital": "Malabo",
        "languages": [
            "Spanish",
            "French"
        ],
        "population": 1222442,
        "flag": "https://restcountries.eu/data/gnq.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Eritrea",
        "capital": "Asmara",
        "languages": [
            "Tigrinya",
            "Arabic",
            "English"
        ],
        "population": 5352000,
        "flag": "https://restcountries.eu/data/eri.svg",
        "currency": "Eritrean nakfa"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": [
            "Estonian"
        ],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "languages": [
            "Amharic"
        ],
        "population": 92206005,
        "flag": "https://restcountries.eu/data/eth.svg",
        "currency": "Ethiopian birr"
    },
    {
        "name": "Falkland Islands (Malvinas)",
        "capital": "Stanley",
        "languages": [
            "English"
        ],
        "population": 2563,
        "flag": "https://restcountries.eu/data/flk.svg",
        "currency": "Falkland Islands pound"
    },
    {
        "name": "Faroe Islands",
        "capital": "Tórshavn",
        "languages": [
            "Faroese"
        ],
        "population": 49376,
        "flag": "https://restcountries.eu/data/fro.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Fiji",
        "capital": "Suva",
        "languages": [
            "English",
            "Fijian",
            "Hindi",
            "Urdu"
        ],
        "population": 867000,
        "flag": "https://restcountries.eu/data/fji.svg",
        "currency": "Fijian dollar"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": [
            "Finnish",
            "Swedish"
        ],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "France",
        "capital": "Paris",
        "languages": [
            "French"
        ],
        "population": 66710000,
        "flag": "https://restcountries.eu/data/fra.svg",
        "currency": "Euro"
    },
    {
        "name": "French Guiana",
        "capital": "Cayenne",
        "languages": [
            "French"
        ],
        "population": 254541,
        "flag": "https://restcountries.eu/data/guf.svg",
        "currency": "Euro"
    },
    {
        "name": "French Polynesia",
        "capital": "Papeetē",
        "languages": [
            "French"
        ],
        "population": 271800,
        "flag": "https://restcountries.eu/data/pyf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "French Southern Territories",
        "capital": "Port-aux-Français",
        "languages": [
            "French"
        ],
        "population": 140,
        "flag": "https://restcountries.eu/data/atf.svg",
        "currency": "Euro"
    },
    {
        "name": "Gabon",
        "capital": "Libreville",
        "languages": [
            "French"
        ],
        "population": 1802278,
        "flag": "https://restcountries.eu/data/gab.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Gambia",
        "capital": "Banjul",
        "languages": [
            "English"
        ],
        "population": 1882450,
        "flag": "https://restcountries.eu/data/gmb.svg",
        "currency": "Gambian dalasi"
    },
    {
        "name": "Georgia",
        "capital": "Tbilisi",
        "languages": [
            "Georgian"
        ],
        "population": 3720400,
        "flag": "https://restcountries.eu/data/geo.svg",
        "currency": "Georgian Lari"
    },
    {
        "name": "Germany",
        "capital": "Berlin",
        "languages": [
            "German"
        ],
        "population": 81770900,
        "flag": "https://restcountries.eu/data/deu.svg",
        "currency": "Euro"
    },
    {
        "name": "Ghana",
        "capital": "Accra",
        "languages": [
            "English"
        ],
        "population": 27670174,
        "flag": "https://restcountries.eu/data/gha.svg",
        "currency": "Ghanaian cedi"
    },
    {
        "name": "Gibraltar",
        "capital": "Gibraltar",
        "languages": [
            "English"
        ],
        "population": 33140,
        "flag": "https://restcountries.eu/data/gib.svg",
        "currency": "Gibraltar pound"
    },
    {
        "name": "Greece",
        "capital": "Athens",
        "languages": [
            "Greek (modern)"
        ],
        "population": 10858018,
        "flag": "https://restcountries.eu/data/grc.svg",
        "currency": "Euro"
    },
    {
        "name": "Greenland",
        "capital": "Nuuk",
        "languages": [
            "Kalaallisut"
        ],
        "population": 55847,
        "flag": "https://restcountries.eu/data/grl.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Grenada",
        "capital": "St. George's",
        "languages": [
            "English"
        ],
        "population": 103328,
        "flag": "https://restcountries.eu/data/grd.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Guadeloupe",
        "capital": "Basse-Terre",
        "languages": [
            "French"
        ],
        "population": 400132,
        "flag": "https://restcountries.eu/data/glp.svg",
        "currency": "Euro"
    },
    {
        "name": "Guam",
        "capital": "Hagåtña",
        "languages": [
            "English",
            "Chamorro",
            "Spanish"
        ],
        "population": 184200,
        "flag": "https://restcountries.eu/data/gum.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "languages": [
            "Spanish"
        ],
        "population": 16176133,
        "flag": "https://restcountries.eu/data/gtm.svg",
        "currency": "Guatemalan quetzal"
    },
    {
        "name": "Guernsey",
        "capital": "St. Peter Port",
        "languages": [
            "English",
            "French"
        ],
        "population": 62999,
        "flag": "https://restcountries.eu/data/ggy.svg",
        "currency": "British pound"
    },
    {
        "name": "Guinea",
        "capital": "Conakry",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 12947000,
        "flag": "https://restcountries.eu/data/gin.svg",
        "currency": "Guinean franc"
    },
    {
        "name": "Guinea-Bissau",
        "capital": "Bissau",
        "languages": [
            "Portuguese"
        ],
        "population": 1547777,
        "flag": "https://restcountries.eu/data/gnb.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Guyana",
        "capital": "Georgetown",
        "languages": [
            "English"
        ],
        "population": 746900,
        "flag": "https://restcountries.eu/data/guy.svg",
        "currency": "Guyanese dollar"
    },
    {
        "name": "Haiti",
        "capital": "Port-au-Prince",
        "languages": [
            "French",
            "Haitian"
        ],
        "population": 11078033,
        "flag": "https://restcountries.eu/data/hti.svg",
        "currency": "Haitian gourde"
    },
    {
        "name": "Heard Island and McDonald Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/hmd.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Holy See",
        "capital": "Rome",
        "languages": [
            "Latin",
            "Italian",
            "French",
            "German"
        ],
        "population": 451,
        "flag": "https://restcountries.eu/data/vat.svg",
        "currency": "Euro"
    },
    {
        "name": "Honduras",
        "capital": "Tegucigalpa",
        "languages": [
            "Spanish"
        ],
        "population": 8576532,
        "flag": "https://restcountries.eu/data/hnd.svg",
        "currency": "Honduran lempira"
    },
    {
        "name": "Hong Kong",
        "capital": "City of Victoria",
        "languages": [
            "English",
            "Chinese"
        ],
        "population": 7324300,
        "flag": "https://restcountries.eu/data/hkg.svg",
        "currency": "Hong Kong dollar"
    },
    {
        "name": "Hungary",
        "capital": "Budapest",
        "languages": [
            "Hungarian"
        ],
        "population": 9823000,
        "flag": "https://restcountries.eu/data/hun.svg",
        "currency": "Hungarian forint"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": [
            "Icelandic"
        ],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": [
            "Hindi",
            "English"
        ],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "languages": [
            "Indonesian"
        ],
        "population": 258705000,
        "flag": "https://restcountries.eu/data/idn.svg",
        "currency": "Indonesian rupiah"
    },
    {
        "name": "Côte d'Ivoire",
        "capital": "Yamoussoukro",
        "languages": [
            "French"
        ],
        "population": 22671331,
        "flag": "https://restcountries.eu/data/civ.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Iran (Islamic Republic of)",
        "capital": "Tehran",
        "languages": [
            "Persian (Farsi)"
        ],
        "population": 79369900,
        "flag": "https://restcountries.eu/data/irn.svg",
        "currency": "Iranian rial"
    },
    {
        "name": "Iraq",
        "capital": "Baghdad",
        "languages": [
            "Arabic",
            "Kurdish"
        ],
        "population": 37883543,
        "flag": "https://restcountries.eu/data/irq.svg",
        "currency": "Iraqi dinar"
    },
    {
        "name": "Ireland",
        "capital": "Dublin",
        "languages": [
            "Irish",
            "English"
        ],
        "population": 6378000,
        "flag": "https://restcountries.eu/data/irl.svg",
        "currency": "Euro"
    },
    {
        "name": "Isle of Man",
        "capital": "Douglas",
        "languages": [
            "English",
            "Manx"
        ],
        "population": 84497,
        "flag": "https://restcountries.eu/data/imn.svg",
        "currency": "British pound"
    },
    {
        "name": "Israel",
        "capital": "Jerusalem",
        "languages": [
            "Hebrew (modern)",
            "Arabic"
        ],
        "population": 8527400,
        "flag": "https://restcountries.eu/data/isr.svg",
        "currency": "Israeli new shekel"
    },
    {
        "name": "Italy",
        "capital": "Rome",
        "languages": [
            "Italian"
        ],
        "population": 60665551,
        "flag": "https://restcountries.eu/data/ita.svg",
        "currency": "Euro"
    },
    {
        "name": "Jamaica",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2723246,
        "flag": "https://restcountries.eu/data/jam.svg",
        "currency": "Jamaican dollar"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "languages": [
            "Japanese"
        ],
        "population": 126960000,
        "flag": "https://restcountries.eu/data/jpn.svg",
        "currency": "Japanese yen"
    },
    {
        "name": "Jersey",
        "capital": "Saint Helier",
        "languages": [
            "English",
            "French"
        ],
        "population": 100800,
        "flag": "https://restcountries.eu/data/jey.svg",
        "currency": "British pound"
    },
    {
        "name": "Jordan",
        "capital": "Amman",
        "languages": [
            "Arabic"
        ],
        "population": 9531712,
        "flag": "https://restcountries.eu/data/jor.svg",
        "currency": "Jordanian dinar"
    },
    {
        "name": "Kazakhstan",
        "capital": "Astana",
        "languages": [
            "Kazakh",
            "Russian"
        ],
        "population": 17753200,
        "flag": "https://restcountries.eu/data/kaz.svg",
        "currency": "Kazakhstani tenge"
    },
    {
        "name": "Kenya",
        "capital": "Nairobi",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 47251000,
        "flag": "https://restcountries.eu/data/ken.svg",
        "currency": "Kenyan shilling"
    },
    {
        "name": "Kiribati",
        "capital": "South Tarawa",
        "languages": [
            "English"
        ],
        "population": 113400,
        "flag": "https://restcountries.eu/data/kir.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "languages": [
            "Arabic"
        ],
        "population": 4183658,
        "flag": "https://restcountries.eu/data/kwt.svg",
        "currency": "Kuwaiti dinar"
    },
    {
        "name": "Kyrgyzstan",
        "capital": "Bishkek",
        "languages": [
            "Kyrgyz",
            "Russian"
        ],
        "population": 6047800,
        "flag": "https://restcountries.eu/data/kgz.svg",
        "currency": "Kyrgyzstani som"
    },
    {
        "name": "Lao People's Democratic Republic",
        "capital": "Vientiane",
        "languages": [
            "Lao"
        ],
        "population": 6492400,
        "flag": "https://restcountries.eu/data/lao.svg",
        "currency": "Lao kip"
    },
    {
        "name": "Latvia",
        "capital": "Riga",
        "languages": [
            "Latvian"
        ],
        "population": 1961600,
        "flag": "https://restcountries.eu/data/lva.svg",
        "currency": "Euro"
    },
    {
        "name": "Lebanon",
        "capital": "Beirut",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 5988000,
        "flag": "https://restcountries.eu/data/lbn.svg",
        "currency": "Lebanese pound"
    },
    {
        "name": "Lesotho",
        "capital": "Maseru",
        "languages": [
            "English",
            "Southern Sotho"
        ],
        "population": 1894194,
        "flag": "https://restcountries.eu/data/lso.svg",
        "currency": "Lesotho loti"
    },
    {
        "name": "Liberia",
        "capital": "Monrovia",
        "languages": [
            "English"
        ],
        "population": 4615000,
        "flag": "https://restcountries.eu/data/lbr.svg",
        "currency": "Liberian dollar"
    },
    {
        "name": "Libya",
        "capital": "Tripoli",
        "languages": [
            "Arabic"
        ],
        "population": 6385000,
        "flag": "https://restcountries.eu/data/lby.svg",
        "currency": "Libyan dinar"
    },
    {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "languages": [
            "German"
        ],
        "population": 37623,
        "flag": "https://restcountries.eu/data/lie.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Lithuania",
        "capital": "Vilnius",
        "languages": [
            "Lithuanian"
        ],
        "population": 2872294,
        "flag": "https://restcountries.eu/data/ltu.svg",
        "currency": "Euro"
    },
    {
        "name": "Luxembourg",
        "capital": "Luxembourg",
        "languages": [
            "French",
            "German",
            "Luxembourgish"
        ],
        "population": 576200,
        "flag": "https://restcountries.eu/data/lux.svg",
        "currency": "Euro"
    },
    {
        "name": "Macao",
        "capital": "",
        "languages": [
            "Chinese",
            "Portuguese"
        ],
        "population": 649100,
        "flag": "https://restcountries.eu/data/mac.svg",
        "currency": "Macanese pataca"
    },
    {
        "name": "Macedonia (the former Yugoslav Republic of)",
        "capital": "Skopje",
        "languages": [
            "Macedonian"
        ],
        "population": 2058539,
        "flag": "https://restcountries.eu/data/mkd.svg",
        "currency": "Macedonian denar"
    },
    {
        "name": "Madagascar",
        "capital": "Antananarivo",
        "languages": [
            "French",
            "Malagasy"
        ],
        "population": 22434363,
        "flag": "https://restcountries.eu/data/mdg.svg",
        "currency": "Malagasy ariary"
    },
    {
        "name": "Malawi",
        "capital": "Lilongwe",
        "languages": [
            "English",
            "Chichewa"
        ],
        "population": 16832910,
        "flag": "https://restcountries.eu/data/mwi.svg",
        "currency": "Malawian kwacha"
    },
    {
        "name": "Malaysia",
        "capital": "Kuala Lumpur",
        "languages": [
            "Malaysian"
        ],
        "population": 31405416,
        "flag": "https://restcountries.eu/data/mys.svg",
        "currency": "Malaysian ringgit"
    },
    {
        "name": "Maldives",
        "capital": "Malé",
        "languages": [
            "Divehi"
        ],
        "population": 344023,
        "flag": "https://restcountries.eu/data/mdv.svg",
        "currency": "Maldivian rufiyaa"
    },
    {
        "name": "Mali",
        "capital": "Bamako",
        "languages": [
            "French"
        ],
        "population": 18135000,
        "flag": "https://restcountries.eu/data/mli.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Malta",
        "capital": "Valletta",
        "languages": [
            "Maltese",
            "English"
        ],
        "population": 425384,
        "flag": "https://restcountries.eu/data/mlt.svg",
        "currency": "Euro"
    },
    {
        "name": "Marshall Islands",
        "capital": "Majuro",
        "languages": [
            "English",
            "Marshallese"
        ],
        "population": 54880,
        "flag": "https://restcountries.eu/data/mhl.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Martinique",
        "capital": "Fort-de-France",
        "languages": [
            "French"
        ],
        "population": 378243,
        "flag": "https://restcountries.eu/data/mtq.svg",
        "currency": "Euro"
    },
    {
        "name": "Mauritania",
        "capital": "Nouakchott",
        "languages": [
            "Arabic"
        ],
        "population": 3718678,
        "flag": "https://restcountries.eu/data/mrt.svg",
        "currency": "Mauritanian ouguiya"
    },
    {
        "name": "Mauritius",
        "capital": "Port Louis",
        "languages": [
            "English"
        ],
        "population": 1262879,
        "flag": "https://restcountries.eu/data/mus.svg",
        "currency": "Mauritian rupee"
    },
    {
        "name": "Mayotte",
        "capital": "Mamoudzou",
        "languages": [
            "French"
        ],
        "population": 226915,
        "flag": "https://restcountries.eu/data/myt.svg",
        "currency": "Euro"
    },
    {
        "name": "Mexico",
        "capital": "Mexico City",
        "languages": [
            "Spanish"
        ],
        "population": 122273473,
        "flag": "https://restcountries.eu/data/mex.svg",
        "currency": "Mexican peso"
    },
    {
        "name": "Micronesia (Federated States of)",
        "capital": "Palikir",
        "languages": [
            "English"
        ],
        "population": 102800,
        "flag": "https://restcountries.eu/data/fsm.svg",
        "currency": "[D]"
    },
    {
        "name": "Moldova (Republic of)",
        "capital": "Chișinău",
        "languages": [
            "Romanian"
        ],
        "population": 3553100,
        "flag": "https://restcountries.eu/data/mda.svg",
        "currency": "Moldovan leu"
    },
    {
        "name": "Monaco",
        "capital": "Monaco",
        "languages": [
            "French"
        ],
        "population": 38400,
        "flag": "https://restcountries.eu/data/mco.svg",
        "currency": "Euro"
    },
    {
        "name": "Mongolia",
        "capital": "Ulan Bator",
        "languages": [
            "Mongolian"
        ],
        "population": 3093100,
        "flag": "https://restcountries.eu/data/mng.svg",
        "currency": "Mongolian tögrög"
    },
    {
        "name": "Montenegro",
        "capital": "Podgorica",
        "languages": [
            "Serbian",
            "Bosnian",
            "Albanian",
            "Croatian"
        ],
        "population": 621810,
        "flag": "https://restcountries.eu/data/mne.svg",
        "currency": "Euro"
    },
    {
        "name": "Montserrat",
        "capital": "Plymouth",
        "languages": [
            "English"
        ],
        "population": 4922,
        "flag": "https://restcountries.eu/data/msr.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Morocco",
        "capital": "Rabat",
        "languages": [
            "Arabic"
        ],
        "population": 33337529,
        "flag": "https://restcountries.eu/data/mar.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Mozambique",
        "capital": "Maputo",
        "languages": [
            "Portuguese"
        ],
        "population": 26423700,
        "flag": "https://restcountries.eu/data/moz.svg",
        "currency": "Mozambican metical"
    },
    {
        "name": "Myanmar",
        "capital": "Naypyidaw",
        "languages": [
            "Burmese"
        ],
        "population": 51419420,
        "flag": "https://restcountries.eu/data/mmr.svg",
        "currency": "Burmese kyat"
    },
    {
        "name": "Namibia",
        "capital": "Windhoek",
        "languages": [
            "English",
            "Afrikaans"
        ],
        "population": 2324388,
        "flag": "https://restcountries.eu/data/nam.svg",
        "currency": "Namibian dollar"
    },
    {
        "name": "Nauru",
        "capital": "Yaren",
        "languages": [
            "English",
            "Nauruan"
        ],
        "population": 10084,
        "flag": "https://restcountries.eu/data/nru.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Nepal",
        "capital": "Kathmandu",
        "languages": [
            "Nepali"
        ],
        "population": 28431500,
        "flag": "https://restcountries.eu/data/npl.svg",
        "currency": "Nepalese rupee"
    },
    {
        "name": "Netherlands",
        "capital": "Amsterdam",
        "languages": [
            "Dutch"
        ],
        "population": 17019800,
        "flag": "https://restcountries.eu/data/nld.svg",
        "currency": "Euro"
    },
    {
        "name": "New Caledonia",
        "capital": "Nouméa",
        "languages": [
            "French"
        ],
        "population": 268767,
        "flag": "https://restcountries.eu/data/ncl.svg",
        "currency": "CFP franc"
    },
    {
        "name": "New Zealand",
        "capital": "Wellington",
        "languages": [
            "English",
            "Māori"
        ],
        "population": 4697854,
        "flag": "https://restcountries.eu/data/nzl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Nicaragua",
        "capital": "Managua",
        "languages": [
            "Spanish"
        ],
        "population": 6262703,
        "flag": "https://restcountries.eu/data/nic.svg",
        "currency": "Nicaraguan córdoba"
    },
    {
        "name": "Niger",
        "capital": "Niamey",
        "languages": [
            "French"
        ],
        "population": 20715000,
        "flag": "https://restcountries.eu/data/ner.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Nigeria",
        "capital": "Abuja",
        "languages": [
            "English"
        ],
        "population": 186988000,
        "flag": "https://restcountries.eu/data/nga.svg",
        "currency": "Nigerian naira"
    },
    {
        "name": "Niue",
        "capital": "Alofi",
        "languages": [
            "English"
        ],
        "population": 1470,
        "flag": "https://restcountries.eu/data/niu.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Norfolk Island",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2302,
        "flag": "https://restcountries.eu/data/nfk.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Korea (Democratic People's Republic of)",
        "capital": "Pyongyang",
        "languages": [
            "Korean"
        ],
        "population": 25281000,
        "flag": "https://restcountries.eu/data/prk.svg",
        "currency": "North Korean won"
    },
    {
        "name": "Northern Mariana Islands",
        "capital": "Saipan",
        "languages": [
            "English",
            "Chamorro"
        ],
        "population": 56940,
        "flag": "https://restcountries.eu/data/mnp.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Norway",
        "capital": "Oslo",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 5223256,
        "flag": "https://restcountries.eu/data/nor.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Oman",
        "capital": "Muscat",
        "languages": [
            "Arabic"
        ],
        "population": 4420133,
        "flag": "https://restcountries.eu/data/omn.svg",
        "currency": "Omani rial"
    },
    {
        "name": "Pakistan",
        "capital": "Islamabad",
        "languages": [
            "English",
            "Urdu"
        ],
        "population": 194125062,
        "flag": "https://restcountries.eu/data/pak.svg",
        "currency": "Pakistani rupee"
    },
    {
        "name": "Palau",
        "capital": "Ngerulmud",
        "languages": [
            "English"
        ],
        "population": 17950,
        "flag": "https://restcountries.eu/data/plw.svg",
        "currency": "[E]"
    },
    {
        "name": "Palestine, State of",
        "capital": "Ramallah",
        "languages": [
            "Arabic"
        ],
        "population": 4682467,
        "flag": "https://restcountries.eu/data/pse.svg",
        "currency": "Israeli new sheqel"
    },
    {
        "name": "Panama",
        "capital": "Panama City",
        "languages": [
            "Spanish"
        ],
        "population": 3814672,
        "flag": "https://restcountries.eu/data/pan.svg",
        "currency": "Panamanian balboa"
    },
    {
        "name": "Papua New Guinea",
        "capital": "Port Moresby",
        "languages": [
            "English"
        ],
        "population": 8083700,
        "flag": "https://restcountries.eu/data/png.svg",
        "currency": "Papua New Guinean kina"
    },
    {
        "name": "Paraguay",
        "capital": "Asunción",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 6854536,
        "flag": "https://restcountries.eu/data/pry.svg",
        "currency": "Paraguayan guaraní"
    },
    {
        "name": "Peru",
        "capital": "Lima",
        "languages": [
            "Spanish"
        ],
        "population": 31488700,
        "flag": "https://restcountries.eu/data/per.svg",
        "currency": "Peruvian sol"
    },
    {
        "name": "Philippines",
        "capital": "Manila",
        "languages": [
            "English"
        ],
        "population": 103279800,
        "flag": "https://restcountries.eu/data/phl.svg",
        "currency": "Philippine peso"
    },
    {
        "name": "Pitcairn",
        "capital": "Adamstown",
        "languages": [
            "English"
        ],
        "population": 56,
        "flag": "https://restcountries.eu/data/pcn.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Poland",
        "capital": "Warsaw",
        "languages": [
            "Polish"
        ],
        "population": 38437239,
        "flag": "https://restcountries.eu/data/pol.svg",
        "currency": "Polish złoty"
    },
    {
        "name": "Portugal",
        "capital": "Lisbon",
        "languages": [
            "Portuguese"
        ],
        "population": 10374822,
        "flag": "https://restcountries.eu/data/prt.svg",
        "currency": "Euro"
    },
    {
        "name": "Puerto Rico",
        "capital": "San Juan",
        "languages": [
            "Spanish",
            "English"
        ],
        "population": 3474182,
        "flag": "https://restcountries.eu/data/pri.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Qatar",
        "capital": "Doha",
        "languages": [
            "Arabic"
        ],
        "population": 2587564,
        "flag": "https://restcountries.eu/data/qat.svg",
        "currency": "Qatari riyal"
    },
    {
        "name": "Republic of Kosovo",
        "capital": "Pristina",
        "languages": [
            "Albanian",
            "Serbian"
        ],
        "population": 1733842,
        "flag": "https://restcountries.eu/data/kos.svg",
        "currency": "Euro"
    },
    {
        "name": "Réunion",
        "capital": "Saint-Denis",
        "languages": [
            "French"
        ],
        "population": 840974,
        "flag": "https://restcountries.eu/data/reu.svg",
        "currency": "Euro"
    },
    {
        "name": "Romania",
        "capital": "Bucharest",
        "languages": [
            "Romanian"
        ],
        "population": 19861408,
        "flag": "https://restcountries.eu/data/rou.svg",
        "currency": "Romanian leu"
    },
    {
        "name": "Russian Federation",
        "capital": "Moscow",
        "languages": [
            "Russian"
        ],
        "population": 146599183,
        "flag": "https://restcountries.eu/data/rus.svg",
        "currency": "Russian ruble"
    },
    {
        "name": "Rwanda",
        "capital": "Kigali",
        "languages": [
            "Kinyarwanda",
            "English",
            "French"
        ],
        "population": 11553188,
        "flag": "https://restcountries.eu/data/rwa.svg",
        "currency": "Rwandan franc"
    },
    {
        "name": "Saint Barthélemy",
        "capital": "Gustavia",
        "languages": [
            "French"
        ],
        "population": 9417,
        "flag": "https://restcountries.eu/data/blm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "capital": "Jamestown",
        "languages": [
            "English"
        ],
        "population": 4255,
        "flag": "https://restcountries.eu/data/shn.svg",
        "currency": "Saint Helena pound"
    },
    {
        "name": "Saint Kitts and Nevis",
        "capital": "Basseterre",
        "languages": [
            "English"
        ],
        "population": 46204,
        "flag": "https://restcountries.eu/data/kna.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Lucia",
        "capital": "Castries",
        "languages": [
            "English"
        ],
        "population": 186000,
        "flag": "https://restcountries.eu/data/lca.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Martin (French part)",
        "capital": "Marigot",
        "languages": [
            "English",
            "French",
            "Dutch"
        ],
        "population": 36979,
        "flag": "https://restcountries.eu/data/maf.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Pierre and Miquelon",
        "capital": "Saint-Pierre",
        "languages": [
            "French"
        ],
        "population": 6069,
        "flag": "https://restcountries.eu/data/spm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "capital": "Kingstown",
        "languages": [
            "English"
        ],
        "population": 109991,
        "flag": "https://restcountries.eu/data/vct.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Samoa",
        "capital": "Apia",
        "languages": [
            "Samoan",
            "English"
        ],
        "population": 194899,
        "flag": "https://restcountries.eu/data/wsm.svg",
        "currency": "Samoan tālā"
    },
    {
        "name": "San Marino",
        "capital": "City of San Marino",
        "languages": [
            "Italian"
        ],
        "population": 33005,
        "flag": "https://restcountries.eu/data/smr.svg",
        "currency": "Euro"
    },
    {
        "name": "Sao Tome and Principe",
        "capital": "São Tomé",
        "languages": [
            "Portuguese"
        ],
        "population": 187356,
        "flag": "https://restcountries.eu/data/stp.svg",
        "currency": "São Tomé and Príncipe dobra"
    },
    {
        "name": "Saudi Arabia",
        "capital": "Riyadh",
        "languages": [
            "Arabic"
        ],
        "population": 32248200,
        "flag": "https://restcountries.eu/data/sau.svg",
        "currency": "Saudi riyal"
    },
    {
        "name": "Senegal",
        "capital": "Dakar",
        "languages": [
            "French"
        ],
        "population": 14799859,
        "flag": "https://restcountries.eu/data/sen.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Serbia",
        "capital": "Belgrade",
        "languages": [
            "Serbian"
        ],
        "population": 7076372,
        "flag": "https://restcountries.eu/data/srb.svg",
        "currency": "Serbian dinar"
    },
    {
        "name": "Seychelles",
        "capital": "Victoria",
        "languages": [
            "French",
            "English"
        ],
        "population": 91400,
        "flag": "https://restcountries.eu/data/syc.svg",
        "currency": "Seychellois rupee"
    },
    {
        "name": "Sierra Leone",
        "capital": "Freetown",
        "languages": [
            "English"
        ],
        "population": 7075641,
        "flag": "https://restcountries.eu/data/sle.svg",
        "currency": "Sierra Leonean leone"
    },
    {
        "name": "Singapore",
        "capital": "Singapore",
        "languages": [
            "English",
            "Malay",
            "Tamil",
            "Chinese"
        ],
        "population": 5535000,
        "flag": "https://restcountries.eu/data/sgp.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Sint Maarten (Dutch part)",
        "capital": "Philipsburg",
        "languages": [
            "Dutch",
            "English"
        ],
        "population": 38247,
        "flag": "https://restcountries.eu/data/sxm.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Slovakia",
        "capital": "Bratislava",
        "languages": [
            "Slovak"
        ],
        "population": 5426252,
        "flag": "https://restcountries.eu/data/svk.svg",
        "currency": "Euro"
    },
    {
        "name": "Slovenia",
        "capital": "Ljubljana",
        "languages": [
            "Slovene"
        ],
        "population": 2064188,
        "flag": "https://restcountries.eu/data/svn.svg",
        "currency": "Euro"
    },
    {
        "name": "Solomon Islands",
        "capital": "Honiara",
        "languages": [
            "English"
        ],
        "population": 642000,
        "flag": "https://restcountries.eu/data/slb.svg",
        "currency": "Solomon Islands dollar"
    },
    {
        "name": "Somalia",
        "capital": "Mogadishu",
        "languages": [
            "Somali",
            "Arabic"
        ],
        "population": 11079000,
        "flag": "https://restcountries.eu/data/som.svg",
        "currency": "Somali shilling"
    },
    {
        "name": "South Africa",
        "capital": "Pretoria",
        "languages": [
            "Afrikaans",
            "English",
            "Southern Ndebele",
            "Southern Sotho",
            "Swati",
            "Tswana",
            "Tsonga",
            "Venda",
            "Xhosa",
            "Zulu"
        ],
        "population": 55653654,
        "flag": "https://restcountries.eu/data/zaf.svg",
        "currency": "South African rand"
    },
    {
        "name": "South Georgia and the South Sandwich Islands",
        "capital": "King Edward Point",
        "languages": [
            "English"
        ],
        "population": 30,
        "flag": "https://restcountries.eu/data/sgs.svg",
        "currency": "British pound"
    },
    {
        "name": "Korea (Republic of)",
        "capital": "Seoul",
        "languages": [
            "Korean"
        ],
        "population": 50801405,
        "flag": "https://restcountries.eu/data/kor.svg",
        "currency": "South Korean won"
    },
    {
        "name": "South Sudan",
        "capital": "Juba",
        "languages": [
            "English"
        ],
        "population": 12131000,
        "flag": "https://restcountries.eu/data/ssd.svg",
        "currency": "South Sudanese pound"
    },
    {
        "name": "Spain",
        "capital": "Madrid",
        "languages": [
            "Spanish"
        ],
        "population": 46438422,
        "flag": "https://restcountries.eu/data/esp.svg",
        "currency": "Euro"
    },
    {
        "name": "Sri Lanka",
        "capital": "Colombo",
        "languages": [
            "Sinhalese",
            "Tamil"
        ],
        "population": 20966000,
        "flag": "https://restcountries.eu/data/lka.svg",
        "currency": "Sri Lankan rupee"
    },
    {
        "name": "Sudan",
        "capital": "Khartoum",
        "languages": [
            "Arabic",
            "English"
        ],
        "population": 39598700,
        "flag": "https://restcountries.eu/data/sdn.svg",
        "currency": "Sudanese pound"
    },
    {
        "name": "Suriname",
        "capital": "Paramaribo",
        "languages": [
            "Dutch"
        ],
        "population": 541638,
        "flag": "https://restcountries.eu/data/sur.svg",
        "currency": "Surinamese dollar"
    },
    {
        "name": "Svalbard and Jan Mayen",
        "capital": "Longyearbyen",
        "languages": [
            "Norwegian"
        ],
        "population": 2562,
        "flag": "https://restcountries.eu/data/sjm.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Swaziland",
        "capital": "Lobamba",
        "languages": [
            "English",
            "Swati"
        ],
        "population": 1132657,
        "flag": "https://restcountries.eu/data/swz.svg",
        "currency": "Swazi lilangeni"
    },
    {
        "name": "Sweden",
        "capital": "Stockholm",
        "languages": [
            "Swedish"
        ],
        "population": 9894888,
        "flag": "https://restcountries.eu/data/swe.svg",
        "currency": "Swedish krona"
    },
    {
        "name": "Switzerland",
        "capital": "Bern",
        "languages": [
            "German",
            "French",
            "Italian"
        ],
        "population": 8341600,
        "flag": "https://restcountries.eu/data/che.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Syrian Arab Republic",
        "capital": "Damascus",
        "languages": [
            "Arabic"
        ],
        "population": 18564000,
        "flag": "https://restcountries.eu/data/syr.svg",
        "currency": "Syrian pound"
    },
    {
        "name": "Taiwan",
        "capital": "Taipei",
        "languages": [
            "Chinese"
        ],
        "population": 23503349,
        "flag": "https://restcountries.eu/data/twn.svg",
        "currency": "New Taiwan dollar"
    },
    {
        "name": "Tajikistan",
        "capital": "Dushanbe",
        "languages": [
            "Tajik",
            "Russian"
        ],
        "population": 8593600,
        "flag": "https://restcountries.eu/data/tjk.svg",
        "currency": "Tajikistani somoni"
    },
    {
        "name": "Tanzania, United Republic of",
        "capital": "Dodoma",
        "languages": [
            "Swahili",
            "English"
        ],
        "population": 55155000,
        "flag": "https://restcountries.eu/data/tza.svg",
        "currency": "Tanzanian shilling"
    },
    {
        "name": "Thailand",
        "capital": "Bangkok",
        "languages": [
            "Thai"
        ],
        "population": 65327652,
        "flag": "https://restcountries.eu/data/tha.svg",
        "currency": "Thai baht"
    },
    {
        "name": "Timor-Leste",
        "capital": "Dili",
        "languages": [
            "Portuguese"
        ],
        "population": 1167242,
        "flag": "https://restcountries.eu/data/tls.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Togo",
        "capital": "Lomé",
        "languages": [
            "French"
        ],
        "population": 7143000,
        "flag": "https://restcountries.eu/data/tgo.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Tokelau",
        "capital": "Fakaofo",
        "languages": [
            "English"
        ],
        "population": 1411,
        "flag": "https://restcountries.eu/data/tkl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Tonga",
        "capital": "Nuku'alofa",
        "languages": [
            "English",
            "Tonga (Tonga Islands)"
        ],
        "population": 103252,
        "flag": "https://restcountries.eu/data/ton.svg",
        "currency": "Tongan paʻanga"
    },
    {
        "name": "Trinidad and Tobago",
        "capital": "Port of Spain",
        "languages": [
            "English"
        ],
        "population": 1349667,
        "flag": "https://restcountries.eu/data/tto.svg",
        "currency": "Trinidad and Tobago dollar"
    },
    {
        "name": "Tunisia",
        "capital": "Tunis",
        "languages": [
            "Arabic"
        ],
        "population": 11154400,
        "flag": "https://restcountries.eu/data/tun.svg",
        "currency": "Tunisian dinar"
    },
    {
        "name": "Turkey",
        "capital": "Ankara",
        "languages": [
            "Turkish"
        ],
        "population": 78741053,
        "flag": "https://restcountries.eu/data/tur.svg",
        "currency": "Turkish lira"
    },
    {
        "name": "Turkmenistan",
        "capital": "Ashgabat",
        "languages": [
            "Turkmen",
            "Russian"
        ],
        "population": 4751120,
        "flag": "https://restcountries.eu/data/tkm.svg",
        "currency": "Turkmenistan manat"
    },
    {
        "name": "Turks and Caicos Islands",
        "capital": "Cockburn Town",
        "languages": [
            "English"
        ],
        "population": 31458,
        "flag": "https://restcountries.eu/data/tca.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Tuvalu",
        "capital": "Funafuti",
        "languages": [
            "English"
        ],
        "population": 10640,
        "flag": "https://restcountries.eu/data/tuv.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Uganda",
        "capital": "Kampala",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 33860700,
        "flag": "https://restcountries.eu/data/uga.svg",
        "currency": "Ugandan shilling"
    },
    {
        "name": "Ukraine",
        "capital": "Kiev",
        "languages": [
            "Ukrainian"
        ],
        "population": 42692393,
        "flag": "https://restcountries.eu/data/ukr.svg",
        "currency": "Ukrainian hryvnia"
    },
    {
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "languages": [
            "Arabic"
        ],
        "population": 9856000,
        "flag": "https://restcountries.eu/data/are.svg",
        "currency": "United Arab Emirates dirham"
    },
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "capital": "London",
        "languages": [
            "English"
        ],
        "population": 65110000,
        "flag": "https://restcountries.eu/data/gbr.svg",
        "currency": "British pound"
    },
    {
        "name": "United States of America",
        "capital": "Washington, D.C.",
        "languages": [
            "English"
        ],
        "population": 323947000,
        "flag": "https://restcountries.eu/data/usa.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Uruguay",
        "capital": "Montevideo",
        "languages": [
            "Spanish"
        ],
        "population": 3480222,
        "flag": "https://restcountries.eu/data/ury.svg",
        "currency": "Uruguayan peso"
    },
    {
        "name": "Uzbekistan",
        "capital": "Tashkent",
        "languages": [
            "Uzbek",
            "Russian"
        ],
        "population": 31576400,
        "flag": "https://restcountries.eu/data/uzb.svg",
        "currency": "Uzbekistani so'm"
    },
    {
        "name": "Vanuatu",
        "capital": "Port Vila",
        "languages": [
            "Bislama",
            "English",
            "French"
        ],
        "population": 277500,
        "flag": "https://restcountries.eu/data/vut.svg",
        "currency": "Vanuatu vatu"
    },
    {
        "name": "Venezuela (Bolivarian Republic of)",
        "capital": "Caracas",
        "languages": [
            "Spanish"
        ],
        "population": 31028700,
        "flag": "https://restcountries.eu/data/ven.svg",
        "currency": "Venezuelan bolívar"
    },
    {
        "name": "Viet Nam",
        "capital": "Hanoi",
        "languages": [
            "Vietnamese"
        ],
        "population": 92700000,
        "flag": "https://restcountries.eu/data/vnm.svg",
        "currency": "Vietnamese đồng"
    },
    {
        "name": "Wallis and Futuna",
        "capital": "Mata-Utu",
        "languages": [
            "French"
        ],
        "population": 11750,
        "flag": "https://restcountries.eu/data/wlf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "Western Sahara",
        "capital": "El Aaiún",
        "languages": [
            "Spanish"
        ],
        "population": 510713,
        "flag": "https://restcountries.eu/data/esh.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Yemen",
        "capital": "Sana'a",
        "languages": [
            "Arabic"
        ],
        "population": 27478000,
        "flag": "https://restcountries.eu/data/yem.svg",
        "currency": "Yemeni rial"
    },
    {
        "name": "Zambia",
        "capital": "Lusaka",
        "languages": [
            "English"
        ],
        "population": 15933883,
        "flag": "https://restcountries.eu/data/zmb.svg",
        "currency": "Zambian kwacha"
    },
    {
        "name": "Zimbabwe",
        "capital": "Harare",
        "languages": [
            "English",
            "Shona",
            "Northern Ndebele"
        ],
        "population": 14240168,
        "flag": "https://restcountries.eu/data/zwe.svg",
        "currency": "Botswana pula"
    }
]
countrylist=[]
langlist=[]
for i in range(len(countries_data)-1,0,-1):
    if(countries_data[i]['population']==1377422166):
        temp=countries_data[i]
        countries_data[i]=countries_data[0]
        countries_data[0]=temp
        
    for n in range(len(countries_data[i]['languages'])):
            if(countries_data[i]['languages'][n] not in langlist):
                langlist.append(countries_data[i]['languages'][n])
        
for n in range(len(countries_data)-1,0,-1):
    for i in range(n):
        if(countries_data[i]['population'] <= countries_data[i+1]['population']):
            temp=countries_data[i+1]
            countries_data[i+1]=countries_data[i]
            countries_data[i]=temp
print("Top ten most populous countries")
for n in range(10):
    print(countries_data[n]['name'])
print("Top ten most spoken languages")
for n in range(10):
    print(countries_data[n]['languages'])
print(len(langlist))
# Output:
# Top ten most populous countries
# China
# India
# United States of America
# Indonesia
# Brazil
# Pakistan
# Nigeria
# Bangladesh
# Russian Federation
# Japan
# Top ten most spoken languages
# ['Chinese']
# ['Hindi', 'English']
# ['English']
# ['Indonesian']
# ['Portuguese']
# ['English', 'Urdu']
# ['English']
# ['Bengali']
# ['Russian']
# ['Bengali']
# ['Bengali']
# ['Russian']
# ['Bengali']
# ['Russian']
# ['Japanese']
# 112
```
<!-- MARKDOWN-AUTO-DOCS:END -->

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_11/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_11/level1.py -->
```py
def sum(a,b):
    return a+b

print(sum(4,5.6)) #9.6

def aoc(r):
    return 3.14159265359 * (r**2)

print(aoc(2)) #12.56637061436

def sumOfMany(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sumOfMany(1,2,3,4,5,6,7,8,9,10))
# Output: 
# 55

a=['a','b','c','d','e','f','g','h','i','j']

def capitalize_list_items(a):
    return list(map(lambda x: x.upper(), a))
print(capitalize_list_items(a))

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def func1(a, item1):
    a.append(item1)
    return a
print(func1(a,'k'))

def func2(list, item):
    if(item in list):
        list.remove(item)
    return list
listnew=[2,45,68,34,23,56,78,90,12,34,56,78,90]
print(func2(listnew,56))
#Output:
# [2, 45, 68, 34, 23, 78, 90, 12, 34, 56, 78, 90]
def func13(num):
    sum=0
    for i in range(num):
        sum+=i
    return sum

print(func13(10))

#Output:
# 45

def func14(rang1):
    sum=0
    for i in range(rang1):
        if i%2==0:
            sum+=i
    return sum
print(func14(10))
#Output:
# 20

def func15(rang1):
    sum=0
    for i in range(rang1):
        if i%2!=0:
            sum+=i
    return sum
print(func15(10))

#Output:
# 25
```
<!-- MARKDOWN-AUTO-DOCS:END -->