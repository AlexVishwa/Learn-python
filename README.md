_See older readme: [Click here](./README.old.md) (README.old.md)_

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
class bsort:
    def __init__(self,arr):
        self.arr=arr
    def sort(self):
        for n in range(len(self.arr)-1,0,-1):
            for i in range(n):
                if(self.arr[i]>self.arr[i+1]):
                    temp=self.arr[i+1]
                    self.arr[i+1]=self.arr[i]
                    self.arr[i]=temp
        return self.arr

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
    print(nordic_countries.index('India'))
    # print('India' in nordic_countries)
# Works for tuple as well as list, in and not in
except ValueError:
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
from functools import reduce
import os
import json
from pathlib import Path


class day10:
    def __init__():
        sum=0
    def readCountriesDataFromJsonFile():
        dirname = os.path.dirname(os.path.dirname(__file__))
        data_file = os.path.join(dirname, "data", "countries_data.json")

        with open(data_file, "r") as f:
            countries_data = json.load(f)
        return countries_data
    
    def readCountriesFromJsonFile():
        dirname = os.path.dirname(os.path.dirname(__file__))
        data_file = os.path.join(dirname, "data", "countries.json")

        with open(data_file, "r") as f:
            countries = json.load(f)
        return countries
    countries_data=readCountriesDataFromJsonFile()
    countries=readCountriesFromJsonFile()
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

    def most_spoken_langs_most_populous():
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
print(func15())

#Output:
# 25
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_11/level3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_11/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_11/level3.py -->
```py
# import multiprocessing from mp

# def __init__:

def is_prime(num):
    if(num==2):
        print("Prime Number")
    elif(num):
        for i in range(2,num):
            if(num%i==0):
                print("Not Prime Number")
                break
        else:
            print("Prime Number")

# is_prime(20000000000000000000000000000000000000000000000000456678977777987777777777777779466666666666666666666666333333333333333333333333333333333333333333335714389)

def check_list(list1):
    s1=set(list1)
    l1=len(list1)
    l2=len(s1)
    if(l1==l2):
        print("list is unique")
    else:
        print("list ain't unique")

# check_list([1,2,3,3,4,5,6,7,8,9,10])

def checkdt(list1):
    for i in range(len(list1)-1):
        a=type(list1[i])
        if(a==type(list1[i+1])):
            if(i==len(list1)-1):
                print("All elements are of same type")
            pass
        else:
            print("All elements are not of same type")
            break
# checkdt([1,2,3,'alex'])
    
def varname():
    var = input("Enter the variable name:\n")
    if var[0].isnumeric():  # Check if the first character is a number
        print("Variable name is invalid")
        return
    for char in var:  # Iterate through each character in the variable name
        if not (char.isalnum() or char == '_'):  # Only alphanumeric and underscore are valid
            print("Variable name is invalid")
            return
    print("Variable name is valid")

varname()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_11/taylor_expansion.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_11/taylor_expansion.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_11/taylor_expansion.py -->
```py
import math


def taylor_expansion(f, a, x, terms):
    """
    Computes the Taylor series expansion of a function f around x = a up to the given number of terms.

    Parameters:
    - f: Function that returns the nth derivative of f at a.
    - a: Point around which the series is expanded.
    - x: Value at which the series is evaluated.
    - terms: Number of terms to sum in the series.

    Returns:
    - Approximation of f(x) using Taylor series.
    """
    taylor_sum = 0
    for n in range(terms):
        derivative_n = f(a, n)  # Compute nth derivative at a
        term = (derivative_n / math.factorial(n)) * (x - a) ** n
        taylor_sum += term
    return taylor_sum


# Example function: cos(x)
def cos_derivative(a, n):
    """Returns the nth derivative of cos(x) evaluated at x = a."""
    derivatives = [math.cos, math.sin, lambda x: -math.cos(x), lambda x: -math.sin(x)]
    return derivatives[n % 4](a)


# Compute the Taylor series approximation of cos(x) at x = 0.5 using 6 terms
# x = 0.5  # 28.6479 degrees
x = 1  # 57.2958 degrees
# x = 10_000
a = 0  # Maclaurin series
terms = 1
approx_value = taylor_expansion(cos_derivative, a, x, terms)

print(f"Taylor series approximation of cos({x}) using {terms} terms: {approx_value}")
print(f"Actual cos({x}): {math.cos(x)}")
# Taylor series approximation of cos(1) using 10 terms: 0.5403025793650793      
# Actual cos(1): 0.5403023058681398
# Taylor series approximation of cos(1) using 6 terms: 0.5416666666666666       
# Actual cos(1): 0.5403023058681398
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_12/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_12/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_12/level1.py -->
```py
import numpy as np
from scipy import optimize
from random import *
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# if __name__ == "__main__":
#     start = 10
#     end = 50
#     primes = find_primes_in_range(start, end)
#     print(f"Prime numbers between {start} and {end}: {primes}")

def a():
    asciis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    r=randint(0,9)
    s=asciis[randint(0,51)]
    t=asciis[randint(0,51)]
    u=randint(0,9)
    v=asciis[randint(0,51)]
    return f'{r}{s}{t}{u}{v}'

# print(a())

listOfChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a,b=map(int, input("Enter the length and number of Ids").split())
# r=''
# for i in range(b):
#     for j in range(a):
#         r+=str(listOfChars[randint(0,61)])
#     print(r)
#     r=''
# print(r)

def rgbcolorgen():
    return f'rgb({randint(0,255),randint(0,255),randint(0,255)})'
# print(rgbcolorgen())
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_12/level2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_12/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_12/level2.py -->
```py
from random import randint
def hexcodegen(n):
    list1=['A','B','C','D','F','E']
    list2=['0','1','2','3','4','5','6','7','8','9']
    r=''
    for i in range(0,n):
        for j in range(0,3):
            r+=list1[randint(0,5)]+list2[randint(0,9)]
        print(r)
        r=''
    return r

# print(hexcodegen(5))
# f0f0f0

def list_of_rgb_colors(n):
    # i=int(input("Enter the number of colors"))
    list1=[]
    for j in range(n):
        r=f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'
        print(r)
        list1.append(r)
    return list1
# print(list_of_rgb_colors())

def generate_colors():
    # i=int()
    k,j=map(int, input("Enter the number of colors and hex colors").split())
    hexcodegen(k)
    list_of_rgb_colors(j)
generate_colors()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_12/level3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_12/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_12/level3.py -->
```py
import random
from random import randint
def shuffle_the_list():
    # Exercise 1: shuffle the list
    list1 = ["a", "b", "c", "d", "e", "f"]
    # Learn: `random.shuffle` mutates the original array
    random.shuffle(list1)
    return list1

# Exercise 2: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_numbers():
    set1 = set()

    while len(set1) < 7:
        set1.add(randint(0, 9))
    print(set1)
    list1 = list(set1)
    print(list1)

# print(shuffle_the_list())

# list_anon=[1,2,3,4,5,6,7,8,9,10]
# list_anon[randint(0,9)],list_anon[randint(0,9)]=list_anon[randint(0,9)],list_anon[randint(0,9)]
# print(list_anon)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_12/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_12/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_12/level1.py -->
```py
import numpy as np
from scipy import optimize
from random import *
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# if __name__ == "__main__":
#     start = 10
#     end = 50
#     primes = find_primes_in_range(start, end)
#     print(f"Prime numbers between {start} and {end}: {primes}")

def a():
    asciis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    r=randint(0,9)
    s=asciis[randint(0,51)]
    t=asciis[randint(0,51)]
    u=randint(0,9)
    v=asciis[randint(0,51)]
    return f'{r}{s}{t}{u}{v}'

# print(a())

listOfChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a,b=map(int, input("Enter the length and number of Ids").split())
# r=''
# for i in range(b):
#     for j in range(a):
#         r+=str(listOfChars[randint(0,61)])
#     print(r)
#     r=''
# print(r)

def rgbcolorgen():
    return f'rgb({randint(0,255),randint(0,255),randint(0,255)})'
# print(rgbcolorgen())
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/level1.py -->
```py
#Heard about comprehension let's see what's List Comprehension
def negative_integers():
    list1=[-4,-3,-2,-1,0,2,4,6]

    list2=[i for i in list1 if i<=0]

    list3=[i for i in list1 if i==0]

    return list2

def fourD_lists():
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    list1=[item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
    return list1
# print(flatten())

def series():
    list1=[
        (item**1,item**0,item**1, item**2, item**3, item**4, item**5)
        for item in range(11) 
        ]
    return list1
# print(series())

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
#TypeError: 'str' object is not callable

def list_of_dictionaries():
    countries=[
        [
            ("Finland", "Helsinki"),
            ("Sweden", "Stockholm"),
            ("Norway", "Oslo")
        ]
    ]
    lists=[
        {"country":country.upper(),
         "city":capital.upper()
         }
         for inner in countries
         for (country,capital) in inner
         ]
    return lists
# print(list_of_dictionaries())
def concatenation():
    names=[
        [
            ("Asabeneh", "Yetayeh"),
            ("David", "Smith"),
            ("Donald", "Trump")
        ]
    ]
    listnew=[
        first+''+last
        for outer in names
        for first,last in outer
    ]
    return listnew
# print(concatenation())
y= lambda m,x,c: m*x+c
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/level1.py -->
```py
print("------------------------ 1")


# * Mimicing decorator functionality via normal function:
greeting = lambda: "Welcome to Python"


def uppercase_decorator(function):
    return lambda: function().upper()


g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

print("------------------------ 2")

## * Using decorators in python:
# This decorator function is a higher order function that takes a function as a parameter


def uppercase_decorator(function):
    return lambda: function().upper()


# & Learn: The reason is that the decorator syntax @decorator can only be used with function definitions (using def), not with lambda expressions.
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/closure.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/level2.py -->
```py
from functools import reduce
import os
import json
from pathlib import Path

def readCountriesFromJsonFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "countries_data.json")

    with open(data_file, "r") as f:
        countries_data = json.load(f)
    return countries_data


# countries = readCountriesFromJsonFile()
# print(countries)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def q1():
    print(list(map(lambda x: x.upper(),countries)))
# q1()

def q2():
    add=map(lambda x: x**2,numbers)
    print(list(add))
# q2()

def q3():
    print(list(map(lambda x: x.upper(),names)))
# q3()

def q4():
    add=filter(lambda x: x.find('land')!=-1,countries)
    print(list(add))
# q4()

def q5():
    add=filter(lambda x: len(x)-1==6,countries)
    print(list(add))
# q5()

def q6():
    add=filter(lambda x: len(x)-1>=6,countries)
    print(list(add))
q6()

def q7():
    address=filter(lambda text: text.startswith('E'),countries)
    print(list(address))
# q7()
def q8():
    sqnum=map(lambda x: x**2, [i for i in range(10)])
    check_even=filter(lambda x: x%2==0,list(sqnum))
    print(list(check_even))
#q8()
def string_list_items(list1):
    str1=map(lambda x:x,list1)
    print(list(str1))
# string_list_items(['a','b','c','d','e','f','g','h','i','j'])

def reduce1():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    sum= reduce(lambda x,y: x+y,numbers)
    print(sum)
# reduce1()



def joinCountriesProperly(accumulator, current):
    isLastElement = current == countries[-1]
    if isLastElement:
        return accumulator + ", and " + current
    return accumulator + ", " + current

# print(reduce(joinCountriesProperly, countries) + " are north European countries")
# Estonia,Finland,Sweden,Denmark,Norway,Iceland
# def 

def similiar(c):
    # print(c[0]['name'])
    add=filter(lambda item: item['name'].find('ia')!=-1,c)
    print(list(add))
# similiar(countries)

def get_first_ten_countries():
    for i in range(10):
        print(countries[i]['name'])
# get_first_ten_countries()

def get_last_ten_countries():
    for i in range(-1,-11,-1):
        print(countries[i]['name'])
# get_last_ten_countries()
# print(countries)

def get_first_letter_count(country_list):
    dictionary = {}
    for country in country_list:
        firstLetterOfCountry = country['name'][0]
        # & Learn: We use `dictionary.get()` method because if we use dictionary["someBadKey"] then we get exception ---  `KeyError: 'bad_key'`
        dictionary[firstLetterOfCountry] = dictionary.get(firstLetterOfCountry, 0) + 1
    return dictionary


# print(get_first_letter_count(countries))
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/level3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/level3.py -->
```py
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

#     Sort countries by name, by capital, by population
#     Sort out the ten most spoken languages by location.
#     Sort out the ten most populated countries.
from functools import reduce
import os
import json
from pathlib import Path

def readCountriesFromJsonFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "countries_data.json")

    with open(data_file, "r") as f:
        countries_data = json.load(f)
    return countries_data

countries=readCountriesFromJsonFile()

def sort_by_name():
    list11 = map(lambda country: country.get('name', ''), countries)
    print(list(list11).sort())
# sort_by_name()

def sort_by_capital():
    list11 = map(lambda country: country.get('capital', ''), countries)
    print(list(list11).sort())
# sort_by_capital()

def sort_by_population():
    sorted_countries = sorted(countries, key=lambda country: country.get('population', 0), reverse=True)
    result = list(map(lambda country: country.get('name', ''), sorted_countries))
    for i in range(10):
        print(result[i])
sort_by_population()
#Ten most populated countries
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

# def sort_by_language():
#     sorted_countries = sorted(countries, key=lambda country: country.get('languages', 0))
#     result = list(map(lambda country: country.get('name', ''), sorted_countries))
#     print(result)
# sort_by_language()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/filter.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/filter.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/filter.py -->
```py
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria. It returns an iterator object. We can convert the iterator object to a list, tuple, or set.
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

even_numbers = filter(lambda num: num%2==0, numbers)
#Warn if even_numbers directly printed it will give filter address object
print(list(even_numbers))       # [2, 4]

numbers = [1, 2, 3, 4, 5]  # iterable

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

odd_numbers = filter(lambda num: num%2 !=0, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
# def is_name_long(name):
#     if len(name) > 7:
#         return True
#     return False

long_names = filter(lambda name: len(name) > 7, names)
print(list(long_names))         # ['Asabeneh']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/decorator.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/decorator.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/decorator.py -->
```py
#These decorator functions are higher order functions 
# that take functions as parameters
# Applying Multiple Decorators to a Single Function


# First Decorator
def uppercase_decorator(greetFn):
    print("1 - uppercase_decorator body")
    uppercaseFn = lambda: greetFn().upper()
    return uppercaseFn


# Second decorator
def split_string_decorator(uppercaseFn):
    print("2 - split_string_decorator body")
    resultFn = lambda: uppercaseFn().split()
    return resultFn


@split_string_decorator  # * 2nd
@uppercase_decorator  # * 1st
def greeting():  # * 3rd
    print("3 - greetingFunction body")
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
```
<!-- MARKDOWN-AUTO-DOCS:END -->
## File - `30-days-python-asabeneh/day_14/map,array,f.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/map,array,f.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/map,array,f.py -->
```py
# Map is a high order function that takes a function and iterable as a param
#What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new list.
numberlist = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numberlist)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numberlist)
# print(numbers_int) #Warn-- map address object gets printed
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
# print(numbers_int) #Warn-- map address object gets printed
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
# print(numbers_upper_cased) #Warn-- map address object gets printed
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_15/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_15/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_15/level1.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_16/day_time.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/day_time.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/day_time.py -->
```py
from datetime import datetime,time,date,timedelta
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

# Jan Feb Mar Apr Jun Jul Aug Sep Oct Nov Dec
# 31 28,29 31 30 31 30 31 31 30 31 30 31 days
# 52 weeks
# 365, 366 days 12 months
# 52,53 Sat,Sun,Mon,Tue,Wed,Thu,Fri
# 7 days in a week
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_16/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/level1.py -->
```py
from datetime import datetime,date

# datetimenow = datetime.now()
# print(datetimenow)                      # 2021-07-08 07:34:46.549883
# day = datetimenow.day                   # 8
# month = datetimenow.month               # 7
# year = datetimenow.year                 # 2021
# hour = datetimenow.hour                 # 7
# minute = datetimenow.minute             # 38
# second = datetimenow.second
# timestamp = datetimenow.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# new_year = datetime(2020, 1, 1)
# print(new_year)      # 2020-01-01 00:00:00
# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second
# print(day, month, year, hour, minute) #1 1 2020 0 0
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

#? STRFTIME
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)

#* STRPTIME

now=datetime.now()
# print(now)
# day=now.day
# month=now.month
# second=now.second
# year=now.year
# hour=now.hour
# minute=now.minute
# timestamp=now.timestamp()
# print('timestamp:',timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')
# # %m/%d/%Y, %H:%M:%S
# date_object='December/5/2019, 20:25:10'
# date_string=now.strftime('%B/%d/%Y, %H:%M:%S')
# print(date_string)

date_string='5 December, 2019'
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
time_two = date_object.strftime("%d/%m/%Y, %H:%M:%S")
print(time_two)

# t1=date(year="2025",month="3",day="25")
# t2=date(year="2026",month="1",day="1")
# print(t2-t1)
# TypeError: 'str' object cannot be interpreted as an integer
t1=date(year=2025,month=3,day=25)
t2=date(year=2026,month=1,day=1)
# print(t2-t1)
t3=date(year=1970,month=1,day=1)
print(t3-t1)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/packing_unpacking.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/packing_unpack.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/packing_unpack.py -->
```py
# unpacking a list
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

#* Using list for defining a range
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

#* Unpacking a dictionary
# Used in presenting data in a better way.
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

#* Packing a list
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/spreading_Enumeration.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/spreading_Enumeration.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/spreading_Enumeration.py -->
```py
# ? Similiar to spread(...) operator used in Javascript. Spread helps to unpack the elements of a list or a dictionary.Similiarly it unpacks all the key elements of the form.
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

#* Enumerate
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'] 
for index, i in enumerate(countries):
    # print('hi')
    if(i == 'Finland'):
        print(f'The country {i} has been found at index {index}')

# for index, item in enumerate([20, 30, 40]):
#     print(index, item)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/zip.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/zip.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/zip.py -->
```py
# * Making a dictionary with two lists using zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/level.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/level.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/level.py -->
```py
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# es=['Estonia']
# rs=['Russia']
*countries,es,rs=names
# countries=[]
# args=[0,6]
# for i in range(5):
#     countries.append(names[i])
    
print(countries)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/desc.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/desc.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/desc.py -->
```py
# syntac
# *re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
# match = re.search('first', txt, re.I)
# #match = re.search('first|First', txt)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first
#? re.I tells that compiler shall search in both upper and lower case
# # It return a list
# matches = re.findall('[Ll]anguage', txt, re.I)
# matches = re.findall('Language|language', txt, re.I)
# print(matches)  # ['language', 'Language']

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
# #match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# #print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt2 = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
# print(re.split(' ', txt2)) # splitting using \n - end of line symbol
#['I', 'am', 'teacher', 'and', '', 'I', 'love', 'teaching.\nThere', 'is', 'nothing', 'as', 'rewarding', 'as', 'educating', 'and', 'empowering', 'people.\nI', 'found', 'teaching', 'more', 'interesting', 'than', 'any', 'other', 'jobs.\nDoes', 'this', 'motivate', 
# 'you', 'to', 'be', 'a', 'teacher?']
#yes

regex_pattern = r'an+'
txt3 = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
# print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'banana', 'apple', 'banana']

regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  #*   ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/level1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/level1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/level1.py -->
```py
import re
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
def most_frequent_words(paragraph):
    r = re.split(' ', paragraph)
    unique_words = set(r)  # Use a set to avoid duplicates
    for word in unique_words:
        srch = re.findall(r'\b' + re.escape(word) + r'\b', paragraph)
    print(f'({len(srch)},{word})')
    # print(f'({len(srch)},{r[i]})')
most_frequent_words(paragraph)
txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex_pattern=r'-?\b[0-9]+\b'
matches=re.findall(regex_pattern, txt)
finalmatch=(int(p) for p in matches)
# print(int(matches[len(matches)-1])-int(matches[0]))
# print(type(matches))
# regex_pattern=r'[+|-]*[0-9]{2}'
# matches+=re.findall(regex_pattern,txt)
finalmatch=sorted(finalmatch)
print(finalmatch[len(finalmatch)-1]-finalmatch[0])
#20
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/level2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/level2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/level2.py -->
```py
#working properly
import re
def is_valid_identifier(txt):
    regex_pattern=r'[0-9]'
    match1=re.findall(regex_pattern,txt)
    # print(match1)
    regex_pattern=r'[\!|\@|\#|\$|\%|\^|\&|\*|\(|\)]'
    match2=re.findall(regex_pattern,txt)
    # print(matches)
    regex_pattern=r'[^A-Z]'
    match3=re.findall(regex_pattern,txt)
    # print(match3)
    if match1!=[]:
        return False
    elif match2==[]:
        return True
    elif match3!=[]:
        print('Reached here')
        return True
    else:
        return False
    
    
print(is_valid_identifier('bc'))
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/level3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/level3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/level3.py -->
```py
import re
from level1 import most_frequent_words
sentence = '''%I am@ a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @empo@wering peo@ple. ;I found tea@ching mo@re interesting tha@n any other %jo@bs. %Do@es this mo@tivate yo@u to be a tea@cher!?'''

refined_sentence=re.sub('%|@|$|&|!|#|;','',sentence)
# sentence.replace('%','')
most_frequent_words(refined_sentence)
```
<!-- MARKDOWN-AUTO-DOCS:END -->