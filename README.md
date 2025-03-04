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
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/level2.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_06/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_06/level1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_06/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_06/level2.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level_1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level_1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level_2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level_2.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_07/level3.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_07/level3.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_08/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_08/level1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_09/level1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_09/level1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/1.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/level2.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/level2.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_10/level3.py`
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_10/level3.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->