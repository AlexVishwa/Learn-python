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