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
print(rgbcolorgen())