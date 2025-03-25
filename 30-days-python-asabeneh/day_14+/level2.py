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
    