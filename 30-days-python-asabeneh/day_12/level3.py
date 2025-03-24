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