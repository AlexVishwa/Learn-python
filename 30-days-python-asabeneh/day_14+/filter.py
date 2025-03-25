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