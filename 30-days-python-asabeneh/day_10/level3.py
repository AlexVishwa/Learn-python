
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