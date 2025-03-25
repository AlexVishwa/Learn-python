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
